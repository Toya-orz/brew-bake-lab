from pathlib import Path
from playwright.sync_api import sync_playwright


BASE_URL = "http://127.0.0.1:4173"


def seed(page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    page.evaluate("localStorage.clear()")
    page.reload()
    page.wait_for_load_state("networkidle")
    recovered = page.evaluate(
        """() => JSON.parse(localStorage.getItem("brewBakeLab.coffeeBeans.v1"))[
          "bean-white-chocolate-strawberry"
        ]"""
    )
    assert recovered["name"] == "白巧克力与草莓"
    assert recovered["brewParams"]["pour"]["dose"] == "15.5g"
    assert recovered["brewParams"]["pour"]["stages"][2]["grams"] == "240g"
    assert recovered["brewParams"]["espresso"]["time"] == "20秒"
    page.evaluate(
        """() => {
          const beans = JSON.parse(localStorage.getItem("brewBakeLab.coffeeBeans.v1"));
          delete beans["bean-white-chocolate-strawberry"];
          localStorage.setItem("brewBakeLab.coffeeBeans.v1", JSON.stringify(beans));
        }"""
    )
    page.reload()
    page.wait_for_load_state("networkidle")
    assert page.evaluate(
        """() => Boolean(JSON.parse(localStorage.getItem("brewBakeLab.coffeeBeans.v1"))[
          "bean-white-chocolate-strawberry"
        ])"""
    ) is False
    page.evaluate(
        """() => {
          localStorage.setItem("brewBakeLab.coffeeBeans.v1", JSON.stringify({
            "bean-smoke": {
              id: "bean-smoke",
              name: "测试咖啡豆",
              roaster: "B&B",
              origin: "埃塞俄比亚",
              components: [{ variety: "74110", process: "水洗", ratio: "100%" }],
              roastLevel: "浅烘焙",
              roastDate: "2026-07-20",
              rest: "10–20 天",
              notes: "白花、柑橘、红茶"
            },
            "bean-second": {
              id: "bean-second",
              name: "第二款豆",
              brewParams: {
                pour: {
                  dose: "20g", water: "300g", grind: "中粗", temp: "90°C",
                  stages: [
                    { label: "闷蒸", time: "00:00", grams: "40g" },
                    { label: "第二段", time: "00:40", grams: "180g" },
                    { label: "第三段", time: "01:30", grams: "300g" }
                  ]
                },
                espresso: { dose: "19g", yield: "40g", grind: "刻度 3", temp: "93°C", time: "28秒" }
              }
            }
          }));
          const recipe = applyCoffeeTemplate(createRecipeTemplate({
            type: "drink",
            title: "测试手冲",
            category: "饮品 / 咖啡 / 手冲",
            action: "准备"
          }), "pour-over", "bean-smoke");
          localStorage.setItem("brewBakeLab.customRecipes.v1", JSON.stringify({ [recipe.id]: recipe }));
        }"""
    )
    migrated = page.evaluate(
        """() => preparePourRecipe({
          template: "pour-over",
          params: [
            { type: "咖啡豆", value: "15g" },
            { type: "用水", value: "240g" },
            { type: "注水方案", value: "30克 → 150克 → 240克" }
          ],
          pourStages: [null, null, null]
        }).pourStages.map(stage => stage.grams).join(",")"""
    )
    assert migrated == "30g,150g,240g"


def verify_viewport(browser, width, height, suffix):
    page = browser.new_page(viewport={"width": width, "height": height})
    seed(page)
    page.evaluate("""() => { renderBeanDetail("bean-smoke"); setPage("beanDetail"); }""")
    assert page.locator("#beanMethodGroups").get_by_text("15g", exact=True).first.is_visible()
    assert page.locator("#beanMethodGroups").get_by_text("240g", exact=True).first.is_visible()
    assert page.locator("#beanMethodGroups").get_by_text("30g").is_visible()
    method_buttons = page.locator("#beanMethodGroups header button")
    if width > 680:
        first_button_box = method_buttons.nth(0).bounding_box()
        second_button_box = method_buttons.nth(1).bounding_box()
        assert first_button_box and second_button_box
        assert abs(first_button_box["y"] - second_button_box["y"]) <= 1
        assert abs(first_button_box["width"] - second_button_box["width"]) <= 1
    page.screenshot(path=f"/tmp/brew-bake-pour-{suffix}.png", full_page=True)

    page.locator("#editBeanBrewParams").click()
    assert page.locator("#beanForm").get_attribute("data-bean-edit-mode") == "brew"
    assert page.locator("#beanPourWater").is_visible()
    page.locator("#closeBeanLibrary").click()

    page.evaluate('openBeanLibrary("bean-smoke")')
    dialog = page.locator("#beanLibraryDialog")
    assert dialog.is_visible()
    box = dialog.bounding_box()
    save_box = page.locator("#beanForm button[type=submit]").bounding_box()
    assert box and save_box
    page.screenshot(path=f"/tmp/brew-bake-{suffix}.png", full_page=False)
    assert save_box["y"] + save_box["height"] <= height
    if width <= 680:
        assert page.locator(".bean-form-scroll").evaluate(
            "(node) => node.scrollHeight > node.clientHeight"
        )
    page.locator("#beanNotes").fill("白花、柑橘、红茶、蜂蜜")
    page.locator('[data-bean-edit-mode="brew"]').click()
    assert not page.locator("#beanPourWater").is_hidden()
    assert page.locator("#beanName").is_hidden()
    page.screenshot(path=f"/tmp/brew-bake-brew-editor-{suffix}.png", full_page=False)
    page.locator("#beanPourWater").fill("260g")
    page.locator(".bean-brew-editor").nth(1).locator("summary").click()
    page.locator("#beanEspressoDose").fill("19g")
    page.locator("#beanForm button[type=submit]").click()
    assert (
        page.evaluate(
            """() => JSON.parse(localStorage.getItem("brewBakeLab.coffeeBeans.v1"))["bean-smoke"].notes"""
        )
        == "白花、柑橘、红茶、蜂蜜"
    )
    assert page.evaluate(
        """() => JSON.parse(localStorage.getItem("brewBakeLab.coffeeBeans.v1"))["bean-smoke"].brewParams.pour.water"""
    ) == "260g"
    assert page.locator("#openBackupCenterFromBeans").evaluate(
        "(node) => node.classList.contains('needs-backup')"
    )
    page.evaluate("openBackupCenter()")
    assert "有新更改" in page.locator("#backupLastTime").inner_text()
    page.screenshot(path=f"/tmp/brew-bake-backup-reminder-{suffix}.png", full_page=False)
    with page.expect_download():
        page.locator("#exportAllData").click()
    assert not page.locator("#openBackupCenterFromBeans").evaluate(
        "(node) => node.classList.contains('needs-backup')"
    )
    page.locator("#closeBackupCenter").click()
    page.evaluate("""() => { renderBeanDetail("bean-smoke"); setPage("beanDetail"); }""")
    page.locator('[data-open-brew-guide="pour"]').click()
    assert page.locator("#genericDetail").evaluate("(node) => node.classList.contains('active')")
    assert page.locator("#genericTitle").inner_text() == "三段式手冲"
    assert page.locator("#genericBeanLink strong").get_by_text("测试咖啡豆", exact=True).is_visible()
    assert page.locator("#genericParamTable").get_by_text("260g").is_visible()
    assert page.locator("#genericPourPlanRows").get_by_text("30g", exact=True).is_visible()
    assert page.locator("#genericPourPlanRows").get_by_text("操作", exact=True).first.is_visible()
    assert page.locator("#genericPourPlanRows").get_by_text("判断", exact=True).first.is_visible()
    assert page.locator("#genericPourPlanRows").get_by_text("注意", exact=True).first.is_visible()
    assert page.locator("#genericSaveStatus").inner_text() == ""
    page.screenshot(path=f"/tmp/brew-bake-guide-{suffix}.png", full_page=True)
    page.locator("#coffeeFollowStart").click()
    assert page.locator("#followDialog").is_visible()
    assert page.locator("#followDialogTitle").inner_text() == "闷蒸"
    assert page.locator("#followDialogContent").get_by_text("判断", exact=True).is_visible()
    page.locator("#followClose").click()
    page.locator("[data-method-bean-switch]").select_option("bean-second")
    assert page.locator("#genericParamTable").get_by_text("300g").is_visible()
    assert page.locator("#genericPourPlanRows").get_by_text("40g", exact=True).is_visible()
    assert page.evaluate(
        """() => JSON.parse(localStorage.getItem("brewBakeLab.customRecipes.v1"))[
          Object.keys(JSON.parse(localStorage.getItem("brewBakeLab.customRecipes.v1")))[0]
        ].coffeeBeanId"""
    ) == "bean-smoke"
    page.locator("#genericBack").click()
    assert page.locator("#beanDetail").evaluate("(node) => node.classList.contains('active')")
    assert page.locator("#beanDetailName").inner_text() == "第二款豆"
    page.locator('.nav [data-page="techniques"]').click()
    page.locator('#techniques [data-recipe-id="pour-over-coffee"]').click()
    assert page.locator("#genericTitle").inner_text() == "三段式手冲"
    page.locator("[data-method-bean-switch]").select_option("bean-smoke")
    assert page.locator("#genericParamTable").get_by_text("260g").is_visible()
    page.locator("#genericEdit").click()
    first_method = page.locator("#genericPourPlanRows .pour-plan-method").first
    first_method.fill("中心小圈注水，确保粉床全部润湿。")
    page.locator("#genericSave").click()
    assert "已保存" in page.locator("#genericSaveStatus").inner_text()
    assert (
        page.evaluate(
            """() => JSON.parse(localStorage.getItem("brewBakeLab.genericRecipes.v1"))[
              "pour-over-coffee"
            ].pourPlan[0].method"""
        )
        == "中心小圈注水，确保粉床全部润湿。"
    )
    page.evaluate("""() => { renderBeanDetail("bean-second"); setPage("beanDetail"); }""")
    page.locator('[data-open-brew-guide="espresso"]').click()
    assert page.locator("#genericTitle").inner_text() == "意式浓缩"
    assert "19g → 40g" in page.locator("#genericParamTable").inner_text()
    assert page.locator("#genericStepList").get_by_role("heading", name="开始萃取并计时", exact=True).is_visible()
    page.screenshot(path=f"/tmp/brew-bake-espresso-{suffix}.png", full_page=True)
    expected_columns = 2 if width <= 680 else 3
    assert page.locator("#genericParamTable tbody").evaluate(
        "(node) => getComputedStyle(node).gridTemplateColumns.split(' ').length"
    ) == expected_columns
    page.evaluate("openRecipeCreateDialog()")
    page.locator('[data-recipe-create-mode="note"]').click()
    page.locator("#recipeNoteFile").set_input_files(
        files=[{
            "name": "my-recipe.md",
            "mimeType": "text/markdown",
            "buffer": "# Apple Cake\n鸡蛋*2 低粉100g\n工具：烤箱、电子秤\n1. Mix flour and eggs\n2. Bake until golden".encode(),
        }]
    )
    page.wait_for_function("document.querySelector('#recipeNoteInput').value.includes('Apple Cake')")
    assert "Apple Cake" in page.locator("#recipeNoteInput").input_value()
    assert page.locator("#recipeNoteFileName").inner_text() == "my-recipe.md"
    assert page.locator("#recipeNotePreview").is_visible()
    assert page.locator("#recipeCreateSubmit").inner_text().strip() == "导入并编辑"
    page.locator("#recipeCreateSubmit").click()
    assert page.locator("#genericTitle").inner_text() == "Apple Cake"
    assert page.locator("#genericIngredientList [data-generic-ingredient]").count() == 2
    assert "烤箱" in page.locator("#genericToolList").inner_text()
    assert "电子秤" in page.locator("#genericToolList").inner_text()
    assert page.locator("#genericSave").is_visible()
    page.locator("#genericIngredientList [data-generic-ingredient]").first.locator(".generic-prep-amount").fill("3个")
    page.locator("#genericSave").click()
    assert "3个" in page.locator("#genericIngredientList").inner_text()
    assert "材料" not in page.locator("#genericParamTable").inner_text()
    assert page.locator('.anchor-tabs a[href="#genericSteps"]').is_visible()
    assert page.locator('.anchor-tabs a[href="#genericStates"]').is_hidden()
    page.screenshot(path=f"/tmp/brew-bake-import-prep-{suffix}.png", full_page=True)
    page.evaluate("openRecipeCreateDialog()")
    page.locator('[data-recipe-create-mode="manual"]').click()
    page.locator("#newRecipeTemplate").select_option("cake")
    assert page.locator("#newRecipeCategory").input_value() == "烘焙 / 蛋糕"
    assert page.locator("#newRecipeBeanField").is_hidden()
    page.screenshot(path=f"/tmp/brew-bake-template-picker-{suffix}.png", full_page=True)
    page.locator("#newRecipeTitle").fill("测试蛋糕模板")
    page.locator("#newRecipeAction").fill("称量材料并完成第一步混合。")
    page.locator("#recipeCreateSubmit").click()
    assert page.locator("#genericTitle").inner_text() == "测试蛋糕模板"
    assert "蛋糕糊" in page.locator("#genericParamTable").inner_text()
    assert "夹馅" in page.locator("#genericParamTable").inner_text()
    assert page.locator("#genericStepList .phase-divider").count() == 2
    page.locator("#genericSave").click()
    original_id = page.evaluate("activeGenericRecipeId")
    recipe_count = page.evaluate("Object.keys(loadCustomRecipes()).length")
    page.locator("#duplicateGenericRecipe").click()
    assert page.locator("#genericTitle").inner_text() == "测试蛋糕模板（副本）"
    assert page.evaluate("activeGenericRecipeId") != original_id
    assert page.evaluate("Object.keys(loadCustomRecipes()).length") == recipe_count + 1
    assert page.evaluate("(id) => loadCustomRecipes()[id].title", original_id) == "测试蛋糕模板"
    assert page.locator("#genericSave").is_visible()
    page.close()


with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=True)
    verify_viewport(chromium, 390, 844, "mobile")
    verify_viewport(chromium, 1440, 1000, "desktop")
    chromium.close()

print("Coffee editor and pour-over plan passed mobile and desktop browser checks.")

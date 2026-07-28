from pathlib import Path
from playwright.sync_api import sync_playwright


BASE_URL = "http://127.0.0.1:4173"


def seed(page):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
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
            }
          }));
          const recipe = applyCoffeeTemplate(createRecipeTemplate({
            type: "drink",
            title: "测试手冲",
            category: "饮品 / 咖啡 / 手冲",
            action: "准备"
          }), "pour-over", "bean-smoke");
          const second = applyCoffeeTemplate(createRecipeTemplate({
            type: "drink",
            title: "测试手冲 · 大杯",
            category: "饮品 / 咖啡 / 手冲",
            action: "准备"
          }), "pour-over", "bean-smoke");
          second.id = `${recipe.id}-large`;
          second.params.find(item => item.type === "用水").value = "总水量 300g。";
          second.pourStages = [
            { label: "闷蒸", time: "00:00", grams: "40g" },
            { label: "第二段", time: "00:35", grams: "180g" },
            { label: "第三段", time: "01:20", grams: "300g" }
          ];
          localStorage.setItem("brewBakeLab.customRecipes.v1", JSON.stringify({
            [recipe.id]: recipe,
            [second.id]: second
          }));
          window.__smokeRecipeId = recipe.id;
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
    recipe_id = page.evaluate("window.__smokeRecipeId")
    page.evaluate(
        """recipeId => {
          renderGenericRecipe(recipeId);
          setPage("genericDetail");
        }""",
        recipe_id,
    )
    assert page.locator("#genericPourPlan").is_visible()
    assert page.locator("#genericPourPlanRows [data-pour-stage]").count() == 4
    assert not page.locator("#genericStepList").is_visible()
    assert not page.locator("#genericPhoto").is_visible()
    assert not page.locator("#genericStates").is_visible()
    assert not page.locator("#genericTrouble").is_visible()
    assert page.locator("#genericEdit").inner_text() == "编辑参数"
    assert "自动粉水比 1:16" in page.locator("#genericParamHint").inner_text()
    assert page.locator("#pourPresetSelect option").count() == 2
    page.screenshot(path=f"/tmp/brew-bake-pour-{suffix}.png", full_page=True)

    page.click("#genericEdit")
    water_value = page.locator("#genericParamTable tr").nth(1).locator("td").first
    water_value.fill("总水量 300g。")
    page.locator("[data-pour-stage-grams]").nth(0).fill("40g")
    page.locator("[data-pour-stage-grams]").nth(1).fill("180g")
    page.locator("[data-pour-stage-grams]").nth(2).fill("300g")
    page.click("#genericSave")
    assert page.locator(".pour-plan-grams").nth(2).inner_text() == "300g"
    saved_water = page.evaluate(
        """recipeId => JSON.parse(localStorage.getItem("brewBakeLab.customRecipes.v1"))[recipeId].params.find(item => item.type === "用水").value""",
        recipe_id,
    )
    assert saved_water == "总水量 300g。"
    saved_stages = page.evaluate(
        """recipeId => JSON.parse(localStorage.getItem("brewBakeLab.customRecipes.v1"))[recipeId].pourStages.map(item => item.grams).join(",")""",
        recipe_id,
    )
    assert saved_stages == "40g,180g,300g"
    page.locator("#pourPresetSelect").select_option(f"{recipe_id}-large")
    assert page.locator("#genericTitle").inner_text() == "测试手冲 · 大杯"

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
    page.locator("#beanForm button[type=submit]").click()
    assert (
        page.evaluate(
            """() => JSON.parse(localStorage.getItem("brewBakeLab.coffeeBeans.v1"))["bean-smoke"].notes"""
        )
        == "白花、柑橘、红茶、蜂蜜"
    )
    page.close()


with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=True)
    verify_viewport(chromium, 390, 844, "mobile")
    verify_viewport(chromium, 1440, 1000, "desktop")
    chromium.close()

print("Coffee editor and pour-over plan passed mobile and desktop browser checks.")

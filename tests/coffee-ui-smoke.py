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
    assert page.locator("#beanMethodGroups").get_by_text("15g · 240g").is_visible()
    assert page.locator("#beanMethodGroups").get_by_text("30g").is_visible()
    page.screenshot(path=f"/tmp/brew-bake-pour-{suffix}.png", full_page=True)

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
    page.evaluate("""() => { renderBeanDetail("bean-smoke"); setPage("beanDetail"); }""")
    page.locator('[data-open-brew-guide="pour"]').click()
    assert page.locator("#brewGuideSummary").get_by_text("260g").is_visible()
    page.locator("#brewGuideBean").select_option("bean-second")
    assert page.locator("#brewGuideSummary").get_by_text("300g").is_visible()
    assert page.locator("#brewGuideSteps").get_by_text("40g").is_visible()
    page.close()


with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=True)
    verify_viewport(chromium, 390, 844, "mobile")
    verify_viewport(chromium, 1440, 1000, "desktop")
    chromium.close()

print("Coffee editor and pour-over plan passed mobile and desktop browser checks.")

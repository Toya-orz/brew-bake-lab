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
          localStorage.setItem("brewBakeLab.customRecipes.v1", JSON.stringify({ [recipe.id]: recipe }));
          window.__smokeRecipeId = recipe.id;
        }"""
    )


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
    assert "自动粉水比 1:16" in page.locator("#genericParamHint").inner_text()
    page.screenshot(path=f"/tmp/brew-bake-pour-{suffix}.png", full_page=True)

    page.click("#genericEdit")
    assert page.locator("[data-pour-time]").count() == 4
    page.locator("[data-pour-time]").first.fill("00:05")
    page.click("#addPourStage")
    assert page.locator("[data-pour-time]").count() == 5
    page.locator("[data-delete-pour-stage]").last.click()
    page.click("#genericSave")
    assert page.locator(".pour-plan-time").first.inner_text() == "00:05"
    saved_time = page.evaluate(
        """recipeId => JSON.parse(localStorage.getItem("brewBakeLab.customRecipes.v1"))[recipeId].pourPlan[0].time""",
        recipe_id,
    )
    assert saved_time == "00:05"

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

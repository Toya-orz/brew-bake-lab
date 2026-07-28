import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const html = await readFile(new URL("../index.html", import.meta.url), "utf8");

assert.match(html, /brewBakeLab\.coffeeBeans\.v1/);
assert.match(html, /data-page="beans"><i data-lucide="coffee"><\/i>咖啡豆仓库/);
assert.match(html, /function getBeanComponents\(bean\)/);
assert.match(html, /data-bean-variety/);
assert.match(html, /data-bean-process/);
assert.match(html, /data-bean-ratio/);
assert.match(html, /if \(rows\.length <= 1\)/);
assert.match(html, /\.bean-card strong \{ grid-column: 1; grid-row: 1;/);
assert.match(html, /\.bean-card span \{ grid-column: 1; grid-row: 2;/);
assert.match(html, /\.bean-card > svg \{ grid-row: 1 \/ 3; grid-column: 2;/);
assert.match(html, /id="beanDetail"/);
assert.match(html, /function renderBeanDetail\(beanId\)/);
assert.match(html, /data-new-bean-method="pour-over"/);
assert.match(html, /data-new-bean-method="espresso"/);
assert.match(html, /function openRecipeCreateForBean\(template\)/);
assert.match(html, /recipe\.coffeeBeanId === beanId/);
assert.match(html, /function applyCoffeeTemplate\(recipe, template, coffeeBeanId = ""\)/);
assert.match(html, /value="pour-over">手冲咖啡/);
assert.match(html, /value="espresso">意式半自动/);
assert.match(html, /function renderGenericBeanLink\(recipe, isEditing = false\)/);
assert.match(html, /if \(recipe\.coffeeBeanId === id\) recipe\.coffeeBeanId = ""/);
assert.match(html, /key\?\.startsWith\("brewBakeLab\."\)/);
assert.match(html, /记录香气、酸甜苦、口感与降温后的变化/);
assert.match(html, /记录甜感、酸苦平衡、醇厚度与下一杯调整/);

console.log("Coffee bean profiles, reusable recipe links, and pour-over/espresso templates are present.");

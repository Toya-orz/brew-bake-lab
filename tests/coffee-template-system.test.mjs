import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const html = await readFile(new URL("../index.html", import.meta.url), "utf8");

assert.match(html, /brewBakeLab\.coffeeBeans\.v1/);
assert.match(html, /function applyCoffeeTemplate\(recipe, template, coffeeBeanId = ""\)/);
assert.match(html, /value="pour-over">手冲咖啡/);
assert.match(html, /value="espresso">意式半自动/);
assert.match(html, /function renderGenericBeanLink\(recipe, isEditing = false\)/);
assert.match(html, /if \(recipe\.coffeeBeanId === id\) recipe\.coffeeBeanId = ""/);
assert.match(html, /key\?\.startsWith\("brewBakeLab\."\)/);
assert.match(html, /记录香气、酸甜苦、口感与降温后的变化/);
assert.match(html, /记录甜感、酸苦平衡、醇厚度与下一杯调整/);

console.log("Coffee bean profiles, reusable recipe links, and pour-over/espresso templates are present.");

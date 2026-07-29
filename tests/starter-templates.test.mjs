import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const html = await readFile(new URL("../index.html", import.meta.url), "utf8");

for (const template of ["baking", "bread", "cake", "oven", "drink"]) {
  assert.match(html, new RegExp(`<option value="${template}">`));
}

assert.match(html, /function applyStarterTemplate\(recipe, template\)/);
assert.match(html, /template === "bread"/);
assert.match(html, /template === "cake"/);
assert.match(html, /template === "oven"/);
assert.match(html, /bread: "烘焙 \/ 面包"/);
assert.match(html, /cake: "烘焙 \/ 蛋糕"/);
assert.match(html, /oven: "烤箱料理"/);
assert.match(html, /recipe = applyStarterTemplate\(recipe, template\)/);
assert.match(html, /选择模板，只填写名称和第一步即可开始/);

console.log("Reusable bread, cake, oven, baking, and drink starter templates are present.");

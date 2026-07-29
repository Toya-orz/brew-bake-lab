import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const html = await readFile(new URL("../index.html", import.meta.url), "utf8");

assert.match(html, /id="duplicateGenericRecipe"/);
assert.match(html, /function duplicateGenericRecipe\(\)/);
assert.match(html, /recipe\.id = createRecipeId\(`\$\{source\.title\}-copy`\)/);
assert.match(html, /recipe\.title = `\$\{source\.title\}（副本）`/);
assert.match(html, /recipe\.custom = true/);
assert.match(html, /Object\.keys\(customRecipes\)\.length >= 100/);
assert.match(html, /设备空间不足，无法复制；原菜谱没有变化/);
assert.match(html, /已复制为新菜谱，修改后保存/);
assert.match(html, /a\[href="#genericStates"\]/);
assert.doesNotMatch(html, /anchor-tabs a:nth-child\(3\)/);

console.log("Recipe duplication creates an independent editable custom copy with storage guards.");

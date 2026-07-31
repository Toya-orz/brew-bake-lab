import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const html = await readFile(new URL("../index.html", import.meta.url), "utf8");

for (const recipe of [
  ["cream-scones", "淡奶油蔓越莓司康"],
  ["new-york-soft-cookies", "减糖纽约软曲奇"],
  ["banana-chocolate-cake", "香蕉巧克力蛋糕"],
  ["cream-toast", "重料淡奶油吐司"],
]) {
  assert.match(html, new RegExp(`id: "${recipe[0]}"`));
  assert.match(html, new RegExp(`title: "${recipe[1]}"`));
  assert.match(html, new RegExp(`assets/imported-recipes/[^"]+\\.jpg`));
}

assert.match(html, /const recipeStatusStorageKey = "brewBakeLab\.recipeStatus\.v1"/);
assert.match(html, /function toggleRecipeStatus\(recipeId, field\)/);
assert.match(html, /data-recipe-status="favorite"/);
assert.match(html, /data-recipe-status="made"/);
assert.match(html, /data-recipe-status-filter="favorite"/);
assert.match(html, /data-recipe-status-filter="made"/);
assert.match(html, /persistRecipeStatuses\(statuses\);\s*renderRecipes\("homeRecipes"\)/);
assert.match(html, /\.filter\(\(recipe\) => !\["pour-over", "espresso"\]\.includes\(recipe\.template\)\)/);
assert.doesNotMatch(html, /<h3 class="filter-title">咖啡方式<\/h3>/);
assert.doesNotMatch(html, /<h3 class="filter-title">技法<\/h3>/);
assert.match(html, /id="recipeLibrarySearch"/);
assert.match(html, /data-recipe-category-filter="烘焙"/);
assert.match(html, /id="recipeSort"/);
assert.match(html, /recipeLibraryQuery = event\.target\.value\.trim\(\)\.toLocaleLowerCase\(\)/);
assert.match(html, /activeRecipeCategoryFilter !== "all"/);
assert.match(html, /count\.textContent = `显示 \$\{cards\.length\} 份菜谱`/);
assert.match(html, /document\.querySelector\("\.topbar \.search"\)\.hidden = pageId === "recipes"/);

console.log("Imported recipes, personal states, and technique/library separation are present.");

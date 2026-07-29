import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const html = await readFile(new URL("../index.html", import.meta.url), "utf8");

assert.match(html, /data-recipe-create-mode="note"/);
assert.match(html, /let recipeCreateMode = "note"/);
assert.match(html, /setRecipeCreateMode\("note"\)/);
assert.match(html, /data-recipe-create-mode="note">从笔记导入/);
assert.match(html, /function parseRecipeNote\(note, type\)/);
assert.match(html, /没有识别到编号步骤/);
assert.match(html, /function extractRecipeNoteIngredients\(note\)/);
assert.match(html, /function extractRecipeNoteTools\(note\)/);
assert.match(html, /function renderRecipeNotePreview\(parsed\)/);
assert.match(html, /function syncRecipeNotePreview\(\)/);
assert.match(html, /function buildRecipeFromNote\(parsed\)/);
assert.match(html, /recipeCreateMode === "note" \? "导入并编辑"/);
assert.doesNotMatch(html, /确认创建/);
assert.doesNotMatch(html, />识别笔记</);
assert.match(html, /只在当前设备解析，不会上传/);
assert.match(html, /id="recipeNoteFile"/);
assert.match(html, /function readRecipeNoteFile\(input\)/);
assert.match(html, /file\.size > 1024 \* 1024/);
assert.match(html, /await file\.text\(\)/);
assert.match(html, /function renderGenericPrep\(recipe, isEditing = false\)/);
assert.match(html, /recipe\.ingredients = parsed\.ingredients/);
assert.match(html, /recipe\.tools = parsed\.tools/);
assert.match(html, /source\.ingredients\.length > 60/);
assert.match(html, /source\.tools\.length > 40/);
assert.match(html, /typeof item === "string" \? item : item\?\.name/);

console.log("Structured ingredients, tools, live note preview, and one-step recipe creation guards are present.");

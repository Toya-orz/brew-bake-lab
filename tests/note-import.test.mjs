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
assert.match(html, /function renderRecipeNotePreview\(parsed\)/);
assert.match(html, /function buildRecipeFromNote\(parsed\)/);
assert.match(html, /if \(!parsedRecipeNote\)[\s\S]*renderRecipeNotePreview\(parsedRecipeNote\)/);
assert.match(html, /只在当前设备解析，不会上传/);
assert.match(html, /id="recipeNoteFile"/);
assert.match(html, /function readRecipeNoteFile\(input\)/);
assert.match(html, /file\.size > 1024 \* 1024/);
assert.match(html, /await file\.text\(\)/);

console.log("Local note parsing, preview confirmation, and recipe creation guards are present.");

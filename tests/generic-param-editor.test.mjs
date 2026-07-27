import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const html = await readFile(new URL("../index.html", import.meta.url), "utf8");

assert.match(html, /const genericParamTypeOptions = \{[\s\S]*baking:[\s\S]*drink:/);
assert.match(html, /data-generic-param-type/);
assert.match(html, /data-generic-param-custom/);
assert.match(html, /data-move-generic-param="up"/);
assert.match(html, /data-move-generic-param="down"/);
assert.match(html, /type: getGenericParamType\(row\)/);
assert.match(html, /renderGenericParams\(recipe\.params, recipe\.type, false\);\s*setGenericEditing\(false\)/);

console.log("Generic parameter categories, custom labels, ordering, and save-state rendering guards are present.");

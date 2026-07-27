import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const page = readFileSync(new URL("../index.html", import.meta.url), "utf8");

assert.doesNotMatch(page, /class="recipe-img"\s+style="background-image/);
assert.match(page, /class="recipe-img"><img src=/);
assert.match(page, /loading="\$\{index < 2 \? "eager" : "lazy"\}"/);
assert.match(page, /\.recipe-img img\s*\{[\s\S]*?object-fit:\s*cover/);
assert.match(page, /class="step-media">[\s\S]*?<img src="\$\{escapeHTML\(image\)\}" loading="eager"/);

console.log("Recipe cards and dynamically revealed step images use Safari-safe loading.");

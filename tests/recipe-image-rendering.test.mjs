import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { readdirSync, statSync } from "node:fs";

const page = readFileSync(new URL("../index.html", import.meta.url), "utf8");

assert.doesNotMatch(page, /class="recipe-img"\s+style="background-image/);
assert.match(page, /class="recipe-img"><img src=/);
assert.match(page, /loading="\$\{index < 2 \? "eager" : "lazy"\}"/);
assert.match(page, /\.recipe-img img\s*\{[\s\S]*?object-fit:\s*cover/);
assert.match(page, /class="step-media">[\s\S]*?<img src="\$\{escapeHTML\(image\)\}" loading="eager"/);
assert.ok(statSync(new URL("../assets/pour-over/coffee-bloom.jpg", import.meta.url)).size < 120_000);
assert.ok(statSync(new URL("../assets/pour-over/circular-pour.jpg", import.meta.url)).size < 120_000);
readdirSync(new URL("../assets/recipes/", import.meta.url))
  .filter((name) => name.endsWith(".jpg"))
  .forEach((name) => {
    assert.ok(statSync(new URL(`../assets/recipes/${name}`, import.meta.url)).size < 220_000);
  });

console.log("Recipe cards and dynamically revealed step images use Safari-safe loading.");

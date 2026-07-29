import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { readdirSync, statSync } from "node:fs";

const page = readFileSync(new URL("../index.html", import.meta.url), "utf8");

assert.doesNotMatch(page, /class="recipe-img"\s+style="background-image/);
assert.match(page, /class="recipe-img"><img src=/);
assert.match(page, /loading="\$\{index < 2 \? "eager" : "lazy"\}"/);
assert.match(page, /\.recipe-img img\s*\{[\s\S]*?object-fit:\s*cover/);
assert.match(page, /class="step-media">[\s\S]*?<img src="\$\{escapeHTML\(image\)\}" loading="eager"/);
assert.match(page, /data-generic-state-image="\$\{escapeHTML\(state\.image \|\| ""\)\}"/);
assert.match(page, /state\.image \? `<div class="state-media"><img src="\$\{escapeHTML\(state\.image\)\}" loading="lazy"/);
assert.ok(statSync(new URL("../assets/pour-over/coffee-bloom.jpg", import.meta.url)).size < 120_000);
assert.ok(statSync(new URL("../assets/pour-over/circular-pour.jpg", import.meta.url)).size < 120_000);
readdirSync(new URL("../assets/recipes/", import.meta.url))
  .filter((name) => name.endsWith(".jpg"))
  .forEach((name) => {
    assert.ok(statSync(new URL(`../assets/recipes/${name}`, import.meta.url)).size < 220_000);
  });
const yogurtBreadImages = readdirSync(new URL("../assets/yogurt-flower-bread/", import.meta.url));
assert.deepEqual(
  yogurtBreadImages.sort(),
  ["final-proof.jpg", "finished.jpg", "first-proof.jpg", "windowpane.jpg"]
);
yogurtBreadImages.forEach((name) => {
  assert.ok(statSync(new URL(`../assets/yogurt-flower-bread/${name}`, import.meta.url)).size < 400_000);
  assert.match(page, new RegExp(`assets/yogurt-flower-bread/${name.replace(".", "\\.")}`));
});

console.log("Recipe cards and dynamically revealed step images use Safari-safe loading.");

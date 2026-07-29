import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const html = await readFile(new URL("../index.html", import.meta.url), "utf8");

assert.match(html, /function restoreWhiteChocolateStrawberryBean\(\)/);
assert.match(html, /bean-white-chocolate-strawberry/);
assert.match(html, /name: "白巧克力与草莓"/);
assert.match(html, /dose: "15\.5g"/);
assert.match(html, /water: "240g"/);
assert.match(html, /grind: "刻度 13（百胜图 e6 air）"/);
assert.match(html, /time: "20秒"/);
assert.match(html, /localStorage\.getItem\(recoveredCoffeeBeanKey\)/);
assert.match(html, /localStorage\.setItem\(recoveredCoffeeBeanKey, "1"\)/);

console.log("White Chocolate & Strawberry coffee bean is restored once with recorded brew parameters.");

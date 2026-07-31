import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const serviceWorker = readFileSync(new URL("../service-worker.js", import.meta.url), "utf8");
const page = readFileSync(new URL("../index.html", import.meta.url), "utf8");

assert.match(serviceWorker, /NAVIGATION_TIMEOUT_MS\s*=\s*4000/);
assert.match(serviceWorker, /controller\.abort\(\)/);
assert.match(serviceWorker, /caches\.match\("\.\/index\.html"\)/);
assert.match(page, /updateViaCache:\s*"none"/);
assert.match(page, /serviceWorker\.addEventListener\("controllerchange"/);
assert.doesNotMatch(page, /controllerchange"[\s\S]{0,240}window\.location\.reload\(\)/);
assert.match(page, /statusPill\.textContent = "已更新 · 下次打开生效"/);
assert.doesNotMatch(serviceWorker, /CORE_ASSETS\s*=\s*\[[\s\S]*?assets\/(?:recipes|pour-over)\//);

console.log("PWA updates do not interrupt the active mobile page.");

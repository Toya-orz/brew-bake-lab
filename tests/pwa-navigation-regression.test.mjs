import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const serviceWorker = readFileSync(new URL("../service-worker.js", import.meta.url), "utf8");
const page = readFileSync(new URL("../index.html", import.meta.url), "utf8");

assert.match(serviceWorker, /NAVIGATION_TIMEOUT_MS\s*=\s*4000/);
assert.match(serviceWorker, /controller\.abort\(\)/);
assert.match(serviceWorker, /caches\.match\("\.\/index\.html"\)/);
assert.match(page, /updateViaCache:\s*"none"/);
assert.match(page, /serviceWorker\.addEventListener\("controllerchange"/);
assert.doesNotMatch(serviceWorker, /CORE_ASSETS\s*=\s*\[[\s\S]*?assets\/(?:recipes|pour-over)\//);

console.log("PWA navigation fallback and update synchronization guards are present.");

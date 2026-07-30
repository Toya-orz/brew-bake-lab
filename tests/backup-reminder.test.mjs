import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const html = await readFile(new URL("../index.html", import.meta.url), "utf8");

assert.match(html, /data-backup-trigger/);
assert.match(html, /const lastDataChangeKey = "brewBakeLab\.lastDataChangeAt"/);
assert.match(html, /function backupIsStale\(\)/);
assert.match(html, /function markDataChanged\(\)/);
assert.match(html, /function updateBackupReminder\(\)/);
assert.match(html, /button\.classList\.toggle\("needs-backup", needsBackup\)/);
assert.match(html, /backupIsStale\(\) \? `\$\{label\} · 有新更改`/);
assert.match(html, /localStorage\.setItem\(fullBackupTimeKey, exportedAt\);\s*updateBackupReminder\(\)/);

console.log("Recipe and coffee changes mark backups stale until a full backup is exported.");

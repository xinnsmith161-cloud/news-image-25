// Entry point for "The World" front page, Tuesday 25 November 2026.
//
// The judged artefact is entry.png, a newspaper front page drawn by
// generate.py (Pillow, no network) from news reports verified for
// 24-25 November 2026. This program's only job is to place a copy of
// that image where the grader expects it.
//
// Contract: the destination directory comes from MAKEFUN_OUTPUT_DIR
// when set (local runs), and defaults to /output (the grader's
// container). The directory is created if it does not exist yet,
// and the copy is checked afterwards so a silent partial write
// cannot pass as success.

import { mkdirSync, statSync, copyFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = resolve(here, "entry.png");

const destinationDir =
  process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const destination = resolve(destinationDir, "entry.png");

mkdirSync(destinationDir, { recursive: true });
copyFileSync(source, destination);

const written = statSync(destination).size;
const original = statSync(source).size;
if (written !== original || written === 0) {
  throw new Error(
    `entry.png copy failed: wrote ${written} bytes, expected ${original}`,
  );
}

console.log(`entry.png -> ${destination} (${written} bytes)`);

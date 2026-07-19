# halftone-apply

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/halftone-apply)

## 📊 Project Details

- **Primary Language:** JavaScript
- **Languages Used:** JavaScript, PowerShell, HTML
- **License:** Other
- **Created:** July 19, 2026
- **Last Updated:** July 19, 2026

## 📝 About

# Halftone — Right-click "Apply Comic Style" for Windows

Right-click a video **file** and choose **"Apply Comic Style (Halftone)"**, or
right-click a **folder** and choose **"Comic-style all videos in folder
(Halftone)"** — either way you get comic-stylized copies named
`<name>_comic.mp4`.

It's a small, per-user Windows Explorer context-menu integration. No admin rights
required — it only touches your own user registry hive (`HKCU`).

## Three ways to get the look — pick the right one

| Path | Where | Match | Speed / resolution |
| --- | --- | --- | --- |
| **This renderer** (`render.js` / right-click) | desktop, offline | **Exact** — same WebGL shaders as the tuner | Full source resolution; slower (headless Chromium per frame) |
| **The website tuner** ([index.html](index.html)) | browser | Exact preview; MP4 export is preview-res | Quick, interactive; recording is at preview resolution |
| **`comicify.sh`** (in the `halftone` repo) | terminal, ffmpeg | **Approximation** — flatter/cooler tones, does *not* match the tuner | Fast, pure ffmpeg |

**This repo is the exact-tuner-match path.** Use it when you want the MP4 to look
exactly like the tuner preview at full resolution.

## Exact-match renderer (what you see in the tuner is what you get)

The output now comes from an **offline renderer that runs the SAME WebGL pipeline
as the [Halftone tuner](index.html)** web app — the same shaders, pass order,
uniform values, and 1100&nbsp;px processing cap. So the MP4 is **pixel-faithful to
the tuner's on-screen preview** (deep warm sky, saturated colors popping, rich
inked lines).

This **replaces the old ffmpeg-only preset**, which used a different filter graph
(`edgedetect`/`lutyuv`/`bilateral`) and produced flatter, cooler tones than the
tuner preview. The renderer lives in [`renderer/`](renderer/):

- `renderer/renderer.html` — the WebGL pipeline (copied verbatim from the tuner).
- `renderer/render.js` — the driver: ffprobe → decode frames → run each frame
  through the WebGL pipeline in headless Chromium (via puppeteer) → encode an
  H.264 MP4, upscaled back to source resolution with `flags=lanczos`, original
  audio preserved.

It uses the tuner's **favorite defaults**: saturation 1.60, contrast 1.55,
flatten strength 6 / passes 2, color levels 12, ink threshold 0.80, thickness 1,
darkness 0.85, edges on. Override from the CLI, e.g.
`node renderer/render.js "clip.mp4" --sat 2.0 --lev 8 --no-edges`.

### One-time setup

The renderer needs its dependencies installed once (this downloads puppeteer's
bundled Chromium):

```
cd renderer
npm install
```

## What it does

You right-click `holiday.mp4` → **Apply Comic Style (Halftone)** → a moment later
`holiday_comic.mp4` appears in the same folder. That's it.

For a whole folder, right-click it → **Comic-style all videos in folder
(Halftone)** → every video (`.mp4 .mov .mkv .avi .webm .m4v`, non-recursive) is
rendered into an `output\` subfolder as `<name>_comic.mp4`.

## Usage

### Right-click (Explorer)

- **A file** → *Apply Comic Style (Halftone)* → writes `<name>_comic.mp4` next to it.
- **A folder** → *Comic-style all videos in folder (Halftone)* → writes each
  `<name>_comic.mp4` into an `output\` subfolder of that folder.

### `render-folder.ps1` (double-click friendly)

Batches a folder without installing the right-click menu. Double-click it (it
shows a folder-picker), or run it with paths:

```
powershell -NoProfile -ExecutionPolicy Bypass -File render-folder.ps1 "C:\clips" ["C:\out"]
```

`$args[0]` is the input folder (omit for a folder-picker, or defaults to the
current directory); `$args[1]` is an optional output folder (default
`<input>\output`). It validates node + ffmpeg + `renderer/node_modules/puppeteer`,
shows progress, and pauses at the end.

### `render.js` CLI (single file or folder)

```
# Single file  → "<name>_comic.mp4" next to the input (or --out <file>)
node renderer/render.js "C:\path\to\clip.mp4" [--out out.mp4]

# Folder       → every video → "output\" subfolder (or --out <dir>)
node renderer/render.js "C:\path\to\folder" [--out "C:\out"]
```

In folder mode the renderer reuses **one** headless-Chromium/WebGL context
across all files (it does not relaunch per file), prints per-file progress
(`[2/7] clip.mp4 → …`) and a final summary; one file failing is logged and the
batch continues. Common overrides: `--sat 2.0 --con 1.4 --rad 6 --pass 2
--lev 12 --thr 0.8 --thick 1 --op 0.85 --no-edges`.

## Prerequisites

- **Windows** (10 or 11).
- **ffmpeg** installed and available on your `PATH`.
  - Download: <https://ffmpeg.org/download.html>
  - Or install with winget:
    ```
    winget install Gyan.FFmpeg
    ```
  - Verify it works by opening a terminal and running `ffmpeg -version`.
- **Node.js** installed and available on your `PATH` (the renderer runs on Node).
  - Download: <https://nodejs.org/>
  - Or install with winget:
    ```
    winget install OpenJS.NodeJS.LTS
    ```
  - Verify with `node -version`.
- **One-time** `cd renderer && npm install` (see above) — pulls puppeteer and its
  bundled Chromium into `renderer/node_modules` (not committed to this repo).

## Install

Clone or download this repo, then either:

- **Right-click `install.ps1` → Run with PowerShell**, or
- run in a terminal from the repo folder:
  ```
  powershell -ExecutionPolicy Bypass -File install.ps1
  ```

The installer registers **two** entries:

- the per-**file** verb for these video extensions: `.mp4 .mov .mkv .avi .webm .m4v`, and
- the per-**folder** verb (on any directory) that batches every video inside it.

Both commands point at the workers (`apply-comic.ps1` / `render-folder.ps1`)
using their absolute paths (resolved from where you cloned the repo), so **keep
the repo folder where it is** after installing. If you move it, re-run
`install.ps1`. The workers in turn run `renderer/render.js`, so keep the
`renderer/` folder (and its installed `node_modules`) alongside them.

## Uninstall

- **Right-click `uninstall.ps1` → Run with PowerShell**, or
  ```
  powershell -ExecutionPolicy Bypass -File uninstall.ps1
  ```

This removes only the keys this tool created under `HKCU`.

## How it works (the pipeline)

`apply-comic.ps1` checks for `ffmpeg` and `node`, then runs `renderer/render.js`
on your video. The renderer reproduces the tuner's WebGL pipeline exactly:

1. **Probe** the input (`ffprobe`) for size, fps, and audio.
2. **Decode** frames with ffmpeg to a temp folder (outside the repo), scaled to the
   tuner's processing size — `min(1, 1100/width)` cap, `flags=lanczos` — so every
   pixel-relative parameter (bilateral radius, edge thickness, texel size) matches
   what you see in the preview.
3. **Stylize** each frame in headless Chromium through the exact WebGL passes:
   - **eq** — contrast then saturation (`(c-0.5)*con+0.5`, then mix toward luma by `sat`).
   - **bilateral ×passes** — edge-preserving flatten (radius `rad`, `sigmaR=0.14`,
     `sigmaS=max(rad*0.6,0.6)`), ping-ponged between framebuffers.
   - **composite** — YUV posterize to `levels` (luma floored to L bands, chroma
     centered-rounded so neutrals don't cast) + Sobel ink edges
     (`smoothstep(thr*4, …)`, thickness `thick`) multiplied in at darkness `op`.
4. **Read back** the processed pixels (flipped to top-down) and write PNGs.
5. **Encode** `libx264 -crf 18 -preset medium -pix_fmt yuv420p`, scaling **back up**
   to the source resolution with `flags=lanczos`, muxing the original audio through
   unchanged (`-c:a copy`), fps preserved.

Because the color math runs in the identical WebGL shaders, the MP4 matches the
tuner preview — not ffmpeg's approximation of it. Temp frames are deleted when done.

## Privacy

The tool runs **entirely locally** on your machine. Nothing is uploaded anywhere.
It only reads the video you pick and writes the `_comic.mp4` next to it.

## Scope / permissions

- **Per-user, no admin.** Installs and uninstalls modify only `HKCU`:
  - per-file: `HKCU:\Software\Classes\SystemFileAssociations\<ext>\shell\HalftoneComic`
  - per-folder: `HKCU:\Software\Classes\Directory\shell\HalftoneComicFolder`

## License

Source-visible. Copyright (c) 2026 aaron777collins. **All rights reserved.** See [LICENSE](LICENSE).


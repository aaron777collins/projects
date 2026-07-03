# pickr

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/pickr)
- [Latest Release: v0.10.0](https://github.com/aaron777collins/pickr/releases/tag/v0.10.0) (July 02, 2026)

## 📊 Project Details

- **Primary Language:** TypeScript
- **Languages Used:** TypeScript, Python, Rust, Shell, CSS, HTML
- **License:** MIT License
- **Created:** June 21, 2026
- **Last Updated:** July 02, 2026

## 📝 About

# Pickr

Drag-to-reorder photo/video curation tool with AI helpers. Built with Tauri 2 + React.

Pick the best shots from a folder of photos and videos, reorder them by dragging, and export clean numbered copies. AI badges surface sharpness, near-duplicates, and faces so you can curate fast.

## Install

**Download a pre-built binary** from [Releases](https://github.com/aaron777collins/pickr/releases) — available for Windows, macOS, and Linux.

Or build from source with one command:

```bash
curl -fsSL https://raw.githubusercontent.com/aaron777collins/pickr/main/setup.sh | bash
cd pickr && npm run tauri dev
```

## Features

- **Folder scanner** -- native dialog, scans for JPG/PNG/HEIC/MP4/MOV/AVI/WebM/MKV
- **Thumbnail grid** with responsive layout and lazy loading
- **Drag-and-drop reorder** via dnd-kit
- **Fullscreen lightbox** for photos (zoom/pan) and videos (HTML5 controls)
- **Include / Skip toggle** per item (Space in lightbox, eye icon on thumbnails)
- **Batch operations** -- Include All / Skip All for visible items
- **AI badges** on every thumbnail:
  - Sharpness score (1-10, color-coded green/amber/red)
  - Face count
  - Duplicate group indicator (pHash-based, auto-detected during scan)
- **Smart filters** -- Sharp only, Has faces, Hide duplicates, Skipped only, Per-person
- **Face recognition** -- detect faces, tag with names, find the same person across all photos
- **Person filtering** -- tagged people show as colored chips in the sidebar; click to filter
- **Duplicate detection** -- pHash-based near-duplicate grouping with best-in-group highlighting
- **Search** -- filename search with real-time filtering
- **Export** -- copy selected items to a folder with numbered prefixes (01_, 02_, ...)
- **Auto-save** -- project state (order, selections, face tags) saved to `.pickr/project.json`
- **Project persistence** -- re-open a folder and everything comes back; new files are appended, missing files are dropped
- **Stats bar** -- live count of total, included, skipped, and filtered items
- **Keyboard shortcuts** -- press `?` for the full list
- **Error boundary** -- graceful error recovery
- **Dark mode** by default, toggleable
- **Cross-platform** -- Windows, macOS, and Linux

## Tech Stack

| Layer | Tech |
|-------|------|
| Shell | Tauri 2 (Rust) |
| Frontend | React 19 + TypeScript + Vite |
| Styling | Tailwind CSS v4 + shadcn/ui |
| State | Zustand |
| Drag & drop | dnd-kit |
| AI sidecar | Python 3.10+ (OpenCV, face_recognition/dlib, imagehash, Pillow) |

## Build from Source

### Prerequisites

- Node.js 20+
- Rust (via rustup)
- Python 3.10+
- **Linux:** `sudo apt install cmake build-essential libopenblas-dev liblapack-dev libgtk-3-dev libwebkit2gtk-4.1-dev libsoup-3.0-dev librsvg2-dev ffmpeg`
- **macOS:** `brew install cmake ffmpeg python3`
- **Windows:** Install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/), [CMake](https://cmake.org/download/), and [FFmpeg](https://ffmpeg.org/download.html)

### Install

```bash
git clone https://github.com/aaron777collins/pickr.git && cd pickr

# Frontend
npm install

# Python sidecar
cd sidecar
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -e ".[dev]"            # core features
pip install -e ".[dev,faces]"      # + face recognition (requires cmake + dlib)
cd ..

# Run
npm run tauri dev
```

## Architecture

```
src/                  React frontend (components, stores, features)
src-tauri/            Rust backend (Tauri commands, sidecar spawning)
sidecar/              Python CLI for media analysis
docs/                 Architecture docs + usage guide
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the full architecture and [docs/USAGE.md](docs/USAGE.md) for the user guide.

## License

MIT


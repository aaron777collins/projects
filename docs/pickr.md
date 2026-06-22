# pickr

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/pickr)

## 📊 Project Details

- **Primary Language:** TypeScript
- **Languages Used:** TypeScript, Python, Rust, CSS, HTML
- **License:** MIT License
- **Created:** June 21, 2026
- **Last Updated:** June 21, 2026

## 📝 About

# Pickr

Drag-to-reorder photo/video curation tool with AI helpers. Built with Tauri 2 + React.

Pick the best shots from a folder of photos and videos, reorder them by dragging, and export clean numbered copies. AI badges surface sharpness, near-duplicates, and faces so you can curate fast.

## Features (v0.1)

- **Folder scanner** -- native dialog, scans for JPG/PNG/HEIC/MP4/MOV/AVI/WebM/MKV
- **Thumbnail grid** with responsive layout and lazy loading
- **Drag-and-drop reorder** via dnd-kit
- **Fullscreen lightbox** for photos (zoom/pan) and videos (HTML5 controls)
- **Include / Skip toggle** per item (Space in lightbox, eye icon on thumbnails)
- **AI badges** on every thumbnail:
  - Sharpness score (1-10, color-coded green/amber/red)
  - Face count
  - Duplicate group indicator (pHash-based)
- **Smart filters** -- Sharp only, Has faces, Hide duplicates, Skipped only
- **Face recognition** -- detect faces, tag with names, find the same person across all photos
- **Export** -- copy selected items to a folder with numbered prefixes (01_, 02_, ...)
- **Auto-save** -- project state (order, selections, face tags) saved to `.pickr.json`
- **Dark mode** by default, toggleable

## v2 Roadmap

- Face blurring on export (non-tagged faces Gaussian blurred)
- Aesthetic scoring (NIMA model)
- AI captioning (BLIP-2 / LLaVA)

## Tech Stack

| Layer | Tech |
|-------|------|
| Shell | Tauri 2 (Rust) |
| Frontend | React 19 + TypeScript + Vite |
| Styling | Tailwind CSS v4 + shadcn/ui |
| State | Zustand |
| Drag & drop | dnd-kit |
| AI sidecar | Python 3.10+ (OpenCV, face_recognition/dlib, imagehash, Pillow) |

## Getting Started

### Prerequisites

- Node.js 20+
- Rust (via rustup)
- Python 3.10+
- System deps (Linux): `sudo apt install cmake build-essential libopenblas-dev liblapack-dev libgtk-3-dev libwebkit2gtk-4.1-dev libsoup-3.0-dev librsvg2-dev ffmpeg`

### Setup

```bash
# Frontend
npm install

# Python sidecar
cd sidecar
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"        # core features
pip install -e ".[dev,faces]"  # + face recognition (requires cmake + dlib)
cd ..

# Run
npm run dev          # Vite dev server only (http://localhost:1420)
npm run tauri dev    # full desktop app (compiles Rust on first run)
```

## Architecture

```
src/                  React frontend (components, stores, features)
src-tauri/            Rust backend (Tauri commands, sidecar spawning)
sidecar/              Python CLI for media analysis
docs/                 Architecture docs + usage guide
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the full architecture and [docs/USAGE.md](docs/USAGE.md) for the user journey.

## License

MIT


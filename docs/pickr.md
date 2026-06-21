# pickr

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/pickr)

## 📊 Project Details

- **Primary Language:** TypeScript
- **Languages Used:** TypeScript, CSS, Rust, HTML
- **License:** MIT License
- **Created:** June 21, 2026
- **Last Updated:** June 21, 2026

## 📝 About

# Pickr

Drag-to-reorder photo/video curation tool with AI helpers.

Pick the best shots from a folder, reorder them, and export clean numbered copies. AI badges surface sharpness, duplicates, and faces so you can decide fast.

> **Work in progress** -- not yet functional.

## v1 Scope

- Folder picker (native dialog)
- Thumbnail grid with lazy loading
- Drag-and-drop reorder
- Lightbox preview (photos + video)
- Include / Skip toggle per media item
- AI badges: sharpness, near-duplicate, face count
- Face recognition (group by person)
- Export renamed/numbered copies
- Save / load session (JSON)

## v2 Scope

- Face blurring (privacy export)
- Aesthetic scoring
- AI captioning

## Tech Stack

| Layer | Tech |
|-------|------|
| Shell | Tauri 2 (Rust) |
| Frontend | React 19 + TypeScript + Vite |
| Styling | Tailwind CSS v4 + shadcn/ui |
| State | Zustand |
| DnD | dnd-kit |
| AI sidecar | Python 3.10+ CLI (ONNX Runtime, face_recognition, OpenCV) |

## Development

```bash
npm install          # install frontend deps
npm run dev          # Vite dev server only
npm run tauri dev    # full Tauri app (compiles Rust on first run)
```

## License

MIT


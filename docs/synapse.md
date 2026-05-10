# synapse

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/synapse)

## 📊 Project Details

- **Primary Language:** Svelte
- **Languages Used:** Svelte, TypeScript, JavaScript, CSS, HTML, Dockerfile
- **License:** MIT License
- **Created:** May 07, 2026
- **Last Updated:** May 09, 2026

## 📝 About

# Synapse

A web-based knowledge management app for creating and navigating interconnected markdown notes. Features wiki-style linking, backlinks, tags, full-text search, a quick switcher, and an interactive graph view.

## Features

- **Wiki-style links** — `[[Note Name]]` with autocomplete and click-to-navigate
- **Backlinks** — See all notes that link to the current note
- **Tags** — `#tag` syntax with a visual tag cloud and filtering
- **Full-text search** — Search across all note contents
- **Quick switcher** — `Ctrl+K` / `Cmd+K` for instant fuzzy note switching
- **Graph view** — Force-directed visualization of note connections
- **CodeMirror 6 editor** — Syntax highlighting, auto-save, mobile toolbar
- **Responsive** — Works on desktop and mobile with touch gestures
- **Dark/Light themes** — System-aware with manual toggle

## Quick Start

```bash
npm install
npm run build
node server/index.js --vault /path/to/your/notes
```

Open `http://localhost:5173`

## Development

```bash
npm run dev        # Vite dev server (port 5174, proxies API)
npm run dev:server # API server (port 5173)
npm test           # Unit tests
npm run test:e2e   # E2E tests
```

## Docker

```bash
docker build -t synapse .
docker run -p 5173:5173 -v /path/to/notes:/vault synapse
```

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl/Cmd + K` | Quick switcher |
| `Ctrl/Cmd + S` | Save |
| `Ctrl/Cmd + G` | Graph view |
| `Ctrl/Cmd + \` | Toggle sidebar |
| `Ctrl/Cmd + .` | Toggle backlinks |
| `Ctrl/Cmd + Shift + F` | Search |

## Tech Stack

Svelte 5 · Vite · Tailwind CSS · CodeMirror 6 · d3-force · Node.js

## License

MIT


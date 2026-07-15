# vellum-outpaint

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/vellum-outpaint)
- [Project Homepage](https://outpaint.aaroncollins.info)

## 📊 Project Details

- **Primary Language:** TypeScript
- **Languages Used:** TypeScript, CSS, Dockerfile, HTML
- **License:** MIT License
- **Created:** July 15, 2026
- **Last Updated:** July 15, 2026

## 📝 About

# Vellum

Vellum is an in-browser outpainting studio: it extends the edges of an image
using a diffusion model that runs entirely client-side via WebGPU, so images
never leave your machine. No upload, no backend, no API key — just a static
site and a browser that supports WebGPU.

Live at **[outpaint.aaroncollins.info](https://outpaint.aaroncollins.info)**.

## How it works

- The model runs in the browser via [`onnxruntime-web`](https://github.com/microsoft/onnxruntime)
  on the WebGPU execution provider, with the threaded WASM backend as a
  fallback path.
- All inference happens locally on your GPU — the app has no server
  component beyond serving static files, so there's nothing to upload and
  nothing to leak.
- UI state is managed with [Zustand](https://github.com/pmndrs/zustand).

## Requirements

- A browser with WebGPU support (recent Chrome/Edge; other browsers vary).
- For local development: Node.js 24+ and npm.

## Local development

```bash
npm install
npm run dev
```

Other scripts:

```bash
npm run build    # type-check (tsc -b) + production build to dist/
npm run preview  # serve the production build locally
npm run lint      # oxlint
```

## Deployment

Vellum is a static SPA (Vite build output in `dist/`) with no server runtime.
It's shipped as a two-stage Docker image (Node build → nginx runtime) behind
a central Caddy reverse proxy. See [`deploy/README.md`](./deploy/README.md)
for the full runbook — build/up commands, wiring up the Caddy site block, and
verification steps.

Two things the deployment setup takes care of that are easy to get wrong for
this kind of app:

- **Cross-origin isolation**: `onnxruntime-web`'s threaded/WebGPU backends
  need `crossOriginIsolated` to be `true` in the browser, which requires
  `Cross-Origin-Opener-Policy: same-origin` and a `Cross-Origin-Embedder-Policy`
  response header. The nginx config uses `credentialless` rather than
  `require-corp` for COEP so that cross-origin model downloads (e.g. from
  huggingface.co) still work.
- **`.wasm` MIME type**: served as `application/wasm` explicitly, since a
  wrong content type will make the browser refuse to instantiate the module.

## License

MIT — see [`LICENSE`](./LICENSE).


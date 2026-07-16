# vellum-outpaint

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/vellum-outpaint)
- [Project Homepage](https://outpaint.aaroncollins.info)

## 📊 Project Details

- **Primary Language:** TypeScript
- **Languages Used:** TypeScript, CSS, Dockerfile, HTML
- **License:** MIT License
- **Created:** July 15, 2026
- **Last Updated:** July 16, 2026

## 📝 About

<div align="center">

# ✦ Vellum

### An infinite canvas for Stable Diffusion — outpainting that runs entirely in your browser.

Extend any image past its edges with a diffusion model that executes on **your own GPU** via WebGPU.
No upload. No backend. No API key. Your images never leave your machine.

<br/>

**[→ Launch the studio at outpaint.aaroncollins.info](https://outpaint.aaroncollins.info)**

<br/>

![WebGPU](https://img.shields.io/badge/WebGPU-local%20inference-6C5CE7?style=flat-square)
![Privacy](https://img.shields.io/badge/data-never%20leaves%20your%20device-00B894?style=flat-square)
![Stable Diffusion](https://img.shields.io/badge/Stable%20Diffusion-Turbo%20%26%201.5-FD79A8?style=flat-square)
![React](https://img.shields.io/badge/React-19-61DAFB?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-2D3436?style=flat-square)

</div>

---

## Why Vellum

Most "AI outpainting" tools send your image to a server. Vellum doesn't have one. The entire
diffusion pipeline — text encoder, U-Net, and VAE — is downloaded once and then runs locally on
your graphics card through [`onnxruntime-web`](https://github.com/microsoft/onnxruntime). After the
first load it works **fully offline**, and nothing you paint is ever uploaded, logged, or seen by
anyone but you.

- 🎨 **Infinite canvas** — pan, zoom, and frame any region to extend. Outpaint in every direction.
- 🖼️ **Stamp your own photos** — drop, paste, or import an image, then drag & scale it onto the
  canvas and outpaint around it. The natural starting point for extending a real photograph.
- 🔒 **Truly private** — no server, no account, no telemetry. It's a static site plus your browser.
- ⚡ **Two engines, one click** — pick instant single-step **SD-Turbo** or the classic, fully
  controllable **SD 1.5**.
- 🪄 **Seamless seams** — feathered latent compositing blends new pixels into the existing image so
  joins disappear.
- 🌐 **Bring your own backend (optional)** — point it at a local Automatic1111 / ComfyUI server if
  you'd rather run those weights.
- 💾 **Cached weights** — models are stored in the browser Cache API, so the multi-GB download
  happens only once. **Install Vellum** (address-bar install icon) so the browser grants
  *persistent* storage and the cache is never evicted — see [Persistent weights](#persistent-weights).

## Engines

Choose per-session from the engine picker — no reload required.

| Engine | Runs on | Speed | Control | Download |
|---|---|---|---|---|
| **SD-Turbo** | Your GPU (WebGPU) | ⚡ ~1 step, seconds | Fixed sampler | ~2.5 GB, once |
| **SD 1.5** | Your GPU (WebGPU) | 🐢 multi-step | Steps + guidance scale | ~2.3 GB, once |
| **Remote WebUI** | Your own A1111/ComfyUI | Depends on host | Full | — |
| **Atelier demo** | CPU, no download | Instant | Procedural preview | none |

> **SD 1.5** is the original, non-distilled model: it runs a real multi-step Euler sampler with
> classifier-free guidance for finer, more prompt-faithful results. **SD-Turbo** trades that control
> for one-step speed. Both stay 100% on-device.

## Requirements

- A browser with **WebGPU + `shader-f16`** — recent **Chrome or Edge (113+)** on a discrete GPU is
  the reliable path. The engine picker will tell you if your browser can't run local inference and
  suggests the demo or a remote backend instead.
- For local development: **Node.js 24+** and npm.

## Quick start

```bash
npm install
npm run dev        # http://localhost:5173
```

Other scripts:

```bash
npm run build      # type-check (tsc -b) + production build → dist/
npm run preview    # serve the production build locally
npm run lint       # oxlint
```

## How it works

```
prompt ─▶ CLIP text encoder ─┐
                             ├─▶ U-Net (denoise, N steps) ─▶ latent ─▶ VAE decoder ─▶ pixels
frame pixels ─▶ VAE encoder ─┘                                                          │
                                                                                        ▼
                                                          feathered composite back onto the canvas
```

- **On-device inference** via `onnxruntime-web` on the WebGPU execution provider (threaded WASM as a
  fallback). fp16 weights are packed/unpacked in JS around the GPU tensors.
- **Outpainting** encodes the existing frame into latent space, injects seeded noise scaled by the
  *fidelity* control, denoises, then feather-composites the result so new and old pixels blend.
- **UI state** is a single [Zustand](https://github.com/pmndrs/zustand) store; the canvas, engines,
  and remote backend all sit behind one `DiffusionProvider` interface.

## Placing photos

The **Stamp** tool is the quickest way to start from a real image:

1. Click **Stamp a photo** in the right rail (or the ❖ tool, or **Import**) — or just **drag an
   image onto the canvas**, or **paste** one with ⌘/Ctrl-V.
2. The photo floats on the canvas. **Drag** to position, drag a **corner** to scale (aspect-locked),
   **Flip** to mirror, or **Fit to frame** to snap it into the current outpaint window.
3. Press **Place** (⏎) to commit it — or **Cancel** (Esc) to discard.

Once placed, move the frame past the photo's edge and **Outpaint** to extend it.

## Persistent weights

The engines cache ~2.5 GB of model weights in the browser Cache API, so the download is a one-time
cost. That cache survives page reloads — **but** browsers keep it as *best-effort* storage by
default, and Chrome only exempts an origin from eviction (`navigator.storage.persist()`) once the
site is **installed, bookmarked, or has enough engagement**. On a brand-new visit that grant is
usually declined, so under disk pressure the browser can reclaim the cache and the weights
re-download on a later visit.

Vellum requests persistence on every load and ships an installable PWA manifest to earn the grant;
if the browser still declines, it tells you so (and how to fix it) instead of silently
re-downloading. **The reliable fix: install Vellum** (the install icon in the address bar, or ⋮ →
*Install*) — installed origins get persistent storage, and the cache then sticks forever.

## Deployment

Vellum is a static SPA (Vite output in `dist/`) with **no server runtime**. It ships as a two-stage
Docker image (Node build → nginx) behind a central Caddy reverse proxy. See
[`deploy/README.md`](./deploy/README.md) for the full runbook.

Two things this class of app gets wrong easily, handled here:

- **Cross-origin isolation** — `onnxruntime-web`'s threaded/WebGPU backends need
  `crossOriginIsolated === true`, which requires `Cross-Origin-Opener-Policy: same-origin` plus a
  `Cross-Origin-Embedder-Policy` header. Vellum uses **`credentialless`** COEP so cross-origin model
  downloads (e.g. from huggingface.co) still succeed.
- **`.wasm` MIME type** — served explicitly as `application/wasm`; a wrong content type makes the
  browser refuse to instantiate the module.

## Tech stack

React 19 · TypeScript · Vite · Zustand · onnxruntime-web (WebGPU) · @huggingface/transformers
(CLIP tokenizer) · Stable Diffusion Turbo & 1.5 (fp16 ONNX)

## License

MIT — see [`LICENSE`](./LICENSE). Model weights are distributed by their respective authors on
Hugging Face under their own licenses.

<div align="center"><br/>Built by <a href="https://aaroncollins.info">Aaron Collins</a> · <a href="https://outpaint.aaroncollins.info">outpaint.aaroncollins.info</a></div>


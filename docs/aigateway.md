# aigateway

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/aigateway)

## 📊 Project Details

- **Primary Language:** HTML
- **Languages Used:** HTML, JavaScript, Dockerfile
- **License:** None
- **Created:** May 07, 2026
- **Last Updated:** May 09, 2026

## 📝 About

# AI Gateway - 3-Tier LiteLLM Proxy

A self-hosted LiteLLM proxy that exposes a single OpenAI-compatible API endpoint (`localhost:4000`) backed by three named model tiers — `smart`, `normal`, and `fast` — each with an ordered fallback chain spanning Ollama Cloud, OpenRouter free models, and local Ollama models. The gateway is bound to `127.0.0.1` only and is never exposed to the public internet.

## Quick Start

```bash
# 1. Copy the example config and fill in your keys
cp litellm_config.example.yaml litellm_config.yaml
cp .env.example .env
# Edit litellm_config.yaml: replace YOUR_OPENROUTER_API_KEY and YOUR_LITELLM_MASTER_KEY

# 2. Create the shared Docker network (once)
docker network create internal

# 3. Start the proxy
docker compose up -d

# 4. Verify it's healthy
curl http://localhost:4000/health
```

## The 3 Tiers

### `smart` — Highest capability, highest latency
Prioritizes the most powerful models available. Falls back through GLM Cloud, Qwen3-Coder (480B MoE via OpenRouter), GPT-OSS-120B, Gemma4-31B cloud, and local Gemma4 models. Use this for complex reasoning, code generation, and tasks where quality matters more than speed.

### `normal` — Balanced capability and speed
Starts with fast OpenRouter free-tier models (Qwen3-80B, Gemma4-31B) before falling back to local Ollama models. The right default for most interactive workloads where you want a capable response without the smart-tier latency.

### `fast` — Lowest latency, smallest active parameter count
Targets MoE models with small active parameter counts (Gemma4-26B with 4B active, GPT-OSS-20B with 3.6B active) for near-instant responses. Falls back to small local models (e2b, hermes3, llama3.2) when cloud is unavailable. Use for autocomplete, short classifications, and latency-sensitive tasks.

## Usage

All three tiers share the same OpenAI-compatible endpoint. Set the `model` field to select the tier:

```bash
# Smart — best model available
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "smart", "messages": [{"role": "user", "content": "Explain monads."}]}'

# Normal — balanced default
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "normal", "messages": [{"role": "user", "content": "Summarize this PR."}]}'

# Fast — lowest latency
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "fast", "messages": [{"role": "user", "content": "Complete this line of code."}]}'
```

## Requirements

- Docker with Compose v2
- Ollama running on the host at `localhost:11434` (for local/cloud Ollama models)
- An [OpenRouter](https://openrouter.ai) API key (for the free-tier cloud models)
- A `docker network create internal` network (shared with other containers on the host)


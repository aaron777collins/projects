# openrouterwhitelist

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/openrouterwhitelist)

## 📊 Project Details

- **Primary Language:** TypeScript
- **Languages Used:** TypeScript, CSS, JavaScript, Dockerfile, HTML
- **License:** None
- **Created:** January 24, 2026
- **Last Updated:** January 25, 2026

## 📝 About

# OpenRouter Whitelist Proxy

A lightweight, secure proxy for OpenRouter that provides:

- **Provider/Model Whitelisting**: Control which AI providers and models are accessible
- **Quantization Support**: Request specific quantization levels (fp16, int8, int4)
- **Authentication**: Secure API key authentication for clients
- **Docker Ready**: Easy deployment with Docker Compose
- **OpenAI Compatible**: Works with any OpenAI-compatible client

## Quick Start

### 1. Clone and Configure

```bash
git clone https://github.com/aaron777collins/openrouterwhitelist.git
cd openrouterwhitelist
cp .env.example .env
```

Edit `.env` with your configuration:

```env
# Your OpenRouter API key
OPENROUTER_API_KEY=sk-or-v1-your-key-here

# Internal API key for clients (generate with: openssl rand -hex 32)
PROXY_API_KEY=your-secure-key-here

# Whitelist settings
ALLOWED_PROVIDERS=openai,anthropic,google,meta,mistral
ALLOWED_MODELS=*
```

### 2. Run with Docker Compose

```bash
docker-compose up -d
```

The proxy will be available at `http://localhost:4001`.

### 3. Test the Proxy

```bash
curl http://localhost:4001/health
```

## API Usage

### Chat Completions

```bash
curl -X POST http://localhost:4001/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-Proxy-Key: your-proxy-api-key" \
  -d '{
    "model": "anthropic/claude-3.5-sonnet",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ]
  }'
```

### List Models

```bash
curl http://localhost:4001/v1/models \
  -H "X-Proxy-Key: your-proxy-api-key"
```

### Streaming

```bash
curl -X POST http://localhost:4001/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-Proxy-Key: your-proxy-api-key" \
  -d '{
    "model": "anthropic/claude-3.5-sonnet",
    "messages": [{"role": "user", "content": "Tell me a story"}],
    "stream": true
  }'
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `4001` |
| `HOST` | Server host | `0.0.0.0` |
| `OPENROUTER_API_KEY` | Your OpenRouter API key | Required |
| `OPENROUTER_BASE_URL` | OpenRouter API base URL | `https://openrouter.ai/api/v1` |
| `PROXY_API_KEY` | Internal API key for clients | Required |
| `ALLOWED_PROVIDERS` | Comma-separated allowed providers | `openai,anthropic,google,meta,mistral` |
| `ALLOWED_MODELS` | Comma-separated allowed models (or `*`) | `*` |
| `BLOCKED_MODELS` | Comma-separated blocked models | (empty) |
| `DEFAULT_MODEL` | Default model if none specified | (empty) |
| `QUANTIZATION` | Quantization preference (fp16, int8, int4) | (empty) |
| `ENABLE_LOGGING` | Enable request logging | `true` |
| `LOG_LEVEL` | Log level (debug, info, warn, error) | `info` |
| `RATE_LIMIT_RPM` | Rate limit per minute | `60` |

### Whitelist Patterns

- `*` - Allow all
- `provider/*` - Allow all models from a provider (e.g., `anthropic/*`)
- `provider/model-name` - Allow specific model

Example:
```env
ALLOWED_PROVIDERS=anthropic,openai
ALLOWED_MODELS=anthropic/*,openai/gpt-4-turbo
BLOCKED_MODELS=anthropic/claude-2
```

## Authentication

The proxy requires authentication via one of:

1. **X-Proxy-Key header** (recommended)
   ```
   X-Proxy-Key: your-api-key
   ```

2. **Authorization Bearer header**
   ```
   Authorization: Bearer your-api-key
   ```

The `/health` endpoint is publicly accessible without authentication.

## Endpoints

| Method | Path | Description | Auth |
|--------|------|-------------|------|
| GET | `/` | API info | No |
| GET | `/health` | Health check | No |
| POST | `/v1/chat/completions` | Chat completions | Yes |
| GET | `/v1/models` | List models | Yes |
| GET | `/v1/models/:id` | Get model info | Yes |
| POST | `/v1/completions` | Legacy completions | Yes |
| GET | `/v1/stats` | Proxy statistics | Yes |

## Client Integration

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:4001/v1",
    api_key="your-proxy-api-key"
)

response = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Node.js

```javascript
const response = await fetch('http://localhost:4001/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-Proxy-Key': 'your-proxy-api-key'
  },
  body: JSON.stringify({
    model: 'anthropic/claude-3.5-sonnet',
    messages: [{ role: 'user', content: 'Hello!' }]
  })
});
```

## Development

### Local Development

```bash
npm install
cp .env.example .env
# Edit .env with your keys
npm run dev
```

### Build

```bash
npm run build
npm start
```

## Security

- Never commit `.env` files with real API keys
- Use strong, randomly generated `PROXY_API_KEY` values
- Run behind a reverse proxy (nginx, Caddy) in production
- Consider IP whitelisting for additional security

## License

MIT


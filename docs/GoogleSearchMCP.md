# GoogleSearchMCP

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/GoogleSearchMCP)

## 📊 Project Details

- **Primary Language:** TypeScript
- **Languages Used:** TypeScript, Dockerfile
- **License:** None
- **Created:** September 20, 2025
- **Last Updated:** September 20, 2025

## 📝 About

# MCP Google Search Server

An MCP server exposing Google search as tools that MCP clients can call. Optional n8n webhook integration logs each query and result set.

## Features
- `google_search`: Programmable Search (JSON API) results (title, link, snippet, metadata)
- `fetch_url`: Fetch a URL and return plain text (best-effort extraction)
- Optional n8n webhook on each search or fetch
- WebSocket transport (easy to connect from remote clients)

## Requirements
- Node.js 20+
- A Google Programmable Search Engine (PSE) **cx**
- A Google API **key** with Custom Search JSON API enabled

## Quick Start (Docker)
1. Copy `env.example` to `.env` and fill values:
   ```bash
   cp env.example .env
   ```
2. Start services:
   ```bash
   docker compose up -d --build
   ```
3. The MCP WebSocket server listens on `ws://localhost:3333` (or your container host).

### Environment Variables
- `GOOGLE_API_KEY` – Google API key
- `GOOGLE_CX` – Programmable Search Engine cx id
- `PORT` – WebSocket server port (default 3333)
- `N8N_WEBHOOK_URL` – optional, e.g. `https://n8n.example.com/webhook/xyz` (will POST logs)
- `FETCH_MAX_BYTES` – max bytes to fetch for `fetch_url` (default 1048576)

## Connect from Claude Desktop (example)
Add to your Claude config (e.g., `claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "google-search": {
      "command": "node",
      "args": ["/app/dist/server.js"],
      "transport": {
        "type": "websocket",
        "url": "ws://localhost:3333"
      }
    }
  }
}
```
> Adjust the path/URL for your setup. If running outside Docker, point to your host.

## n8n Integration
Set `N8N_WEBHOOK_URL` and the server will POST events like:
```json
{
  "event": "google_search",
  "timestamp": "2025-09-20T12:34:56.789Z",
  "query": "site:openai.com mcp",
  "params": {"num": 5},
  "results": [
    {"title": "...", "link": "https://...", "snippet": "...", "source": "google"}
  ]
}
```
You can then branch/transform in n8n (store to DB, send Slack, etc.).

## Development
```bash
npm install
npm run dev
```

## Production
```bash
npm run build && npm start
```

## Security Notes
- Rate-limit with Docker/network policy or place behind a reverse proxy.
- Keep your API key secret. Consider restricting it to your IPs.
- Set a tight `GOOGLE_CX` scope to avoid unwanted results.


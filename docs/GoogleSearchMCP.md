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
- A Google Program


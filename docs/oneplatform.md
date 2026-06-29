# oneplatform

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/oneplatform)
- [GitHub Pages Site](http://www.aaroncollins.info/oneplatform/)

## 📊 Project Details

- **Primary Language:** TypeScript
- **Languages Used:** TypeScript, Shell, HCL, JavaScript, HTML, PLpgSQL, MDX, Go Template, Dockerfile, CSS
- **License:** Other
- **Created:** June 10, 2026
- **Last Updated:** June 29, 2026

## 📝 About

# OnePlatform

**Open-source data integration, transformation, and app platform.**

OnePlatform is a free, open-source alternative to Fivetran + n8n + Retool — combined into one cohesive platform. Ingest data from any source, map it to user-defined ontologies, transform and route it through automated pipelines, and build apps on top of it.

## Core Capabilities

- **Data Ingestion** — Pull from APIs, databases, files; receive webhooks; stream real-time feeds
- **Ontology Engine** — Define data schemas, map source data to your models, auto-generate types and APIs
- **Pipeline Automation** — Trigger-based workflows with cron scheduling, event-driven processing, and custom code
- **Code Execution** — Run JavaScript/TypeScript (fast, ~1ms via isolated-vm) or Python/Go/etc. (Docker sandbox)
- **App Platform** — Build and host apps within the platform using the SDK and code editor
- **API Gateway** — Auto-generated REST endpoints with ontology-driven authorization
- **Auth & RBAC** — Entity-level, field-level, and row-level permissions driven by the ontology
- **Plugin System** — Extend everything via plugins: connectors, transformers, destinations, auth providers
- **Logging & Observability** — Distributed tracing (OTEL), metrics (Prometheus), audit trails
- **CLI & SDKs** — API-first: everything the UI does is available via REST API, CLI, and TypeScript SDKs

## Architecture

9 microservices + shared core library, all running as Docker containers:

| Service | Purpose |
|---------|---------|
| Gateway | API routing, rate limiting, auth validation |
| Auth | Users, sessions, OAuth, RBAC |
| Ingestion | Data connectors, webhooks, file uploads |
| Ontology | Schema engine, data mapping, code generation |
| Pipeline | Workflow orchestration, triggers, cron |
| Execution | Sandboxed code execution |
| App | User app hosting and runtime |
| Logging | Centralized logs, audit, metrics |
| Plugin | Plugin lifecycle, hooks, registry |

## Preview

| Dashboard | Pipeline Editor | App Builder |
|-----------|----------------|-------------|
| ![Dashboard — service health, recent runs, and key metrics](docs/images/dashboard.png) | ![Pipeline Editor — visual drag-and-drop node canvas](docs/images/pipeline-editor.png) | ![App Builder — drag-and-drop UI components with live preview](docs/images/app-builder.png) |

> Screenshots will be added once the hosted demo environment is available. The images above show placeholder paths pointing to `docs/images/`.

## Quick Start

```bash
git clone https://github.com/aaron777collins/oneplatform.git
cd oneplatform
cp .env.example .env
docker compose -f docker/docker-compose.yml up -d
```

The platform will be available at `https://localhost` (Caddy provides TLS with a self-signed certificate for local development; your browser will show a security warning that you can safely accept).

## Tech Stack

- **Frontend:** React 18, TypeScript, Tailwind CSS v4, shadcn/ui
- **Backend:** Hono (TypeScript), Node.js
- **Database:** PostgreSQL 16 + PgBouncer
- **Queue/Cache:** Redis 7 + BullMQ
- **Sandbox:** isolated-vm (JS/TS) + Docker containers (Python/Go/etc.)
- **Observability:** OpenTelemetry, Prometheus, Jaeger
- **Monorepo:** Turborepo + pnpm workspaces

## Shared Packages

| Package | Purpose |
|---------|---------|
| `@oneplatform/core` | Shared engine library — DB, auth, queues, logging, types |
| `@oneplatform/sdk` | External app SDK |
| `@oneplatform/app-sdk` | Platform app SDK |
| `@oneplatform/plugin-sdk` | Plugin development SDK |
| `@oneplatform/cli` | CLI tool (`op`) |

## Development

See [DEVELOPMENT-PROCESS.md](./DEVELOPMENT-PROCESS.md) for the full development workflow.

### Prerequisites

- Node.js 22+
- pnpm 9+
- Docker Engine 20.10+ & Docker Compose V2 (`docker compose version` -- V1 `docker-compose` is unsupported)

### Development Setup

```bash
pnpm install
pnpm dev        # Start all services in dev mode
pnpm test       # Run all tests
pnpm lint       # Lint all packages
```

## Documentation

- [Architecture Decisions](./docs/decisions/001-architecture-decisions.md) — All 23 architecture decisions
- [Design Spec](./docs/superpowers/specs/) — Detailed design specifications
- [Development Process](./DEVELOPMENT-PROCESS.md) — How we build and review code

## Learning Resources

- [Quick Start](./docs/QUICKSTART.md) — Get OnePlatform running locally in under 10 minutes
- [Plugin Development](./docs/quickstarts/plugin-quickstart.md) — Build your first connector or transformer plugin
- [App Builder](./docs/quickstarts/app-quickstart.md) — Create and embed your first app

> Interactive tutorials are planned for a future release. Until then, the quickstart guides above provide step-by-step walkthroughs for common workflows.

## License

Business Source License (BSL) — source-available, free to self-host and modify. Converts to MIT License after 4 years.

See [LICENSE](./LICENSE) for details.

License Summary:

oneplatform is licensed under the Business Source License 1.1.

Non-production use is permitted under the terms of the LICENSE file.

Production use, including internal business use, hosted use, or commercial deployment, requires separate written permission or a commercial license from Aaron Collins.

On 2030-06-17, the Licensed Work converts to the MIT License.


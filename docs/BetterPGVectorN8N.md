# BetterPGVectorN8N

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/BetterPGVectorN8N)
- [GitHub Pages Site](http://www.aaroncollins.info/BetterPGVectorN8N/)
- [Latest Release: Release v1.7.3](https://github.com/aaron777collins/BetterPGVectorN8N/releases/tag/v1.7.3) (December 20, 2025)

## 📊 Project Details

- **Primary Language:** TypeScript
- **Languages Used:** TypeScript, Shell, JavaScript
- **License:** None
- **Created:** December 18, 2025
- **Last Updated:** December 20, 2025

## 📝 About

# n8n-nodes-pgvector-advanced

Advanced PGVector nodes for n8n with full CRUD control. No more limitations of the built-in node.

**[View Full Documentation](https://aaron777collins.github.io/BetterPGVectorN8N/)** | [Installation](https://aaron777collins.github.io/BetterPGVectorN8N/installation) | [Quick Start](https://aaron777collins.github.io/BetterPGVectorN8N/quick-start) | [Docker Guide](https://aaron777collins.github.io/BetterPGVectorN8N/docker)

---

## Install in 30 Seconds

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/aaron777collins/BetterPGVectorN8N/main/install.sh)
```

That's it! The installer auto-detects your setup and does the right thing.

<details>
<summary><b>What does the installer do?</b></summary>

The script detects your n8n environment and offers the best option:

| Your Setup | What It Does |
|------------|--------------|
| Docker Compose | Creates persistent setup that survives rebuilds |
| Running Container | Installs directly into the container |
| npm/Local Install | Adds to ~/.n8n/nodes |
| Nothing Found | Creates fresh n8n + pgvector stack |

</details>

<details>
<summary><b>Manual install options</b></summary>

```bash
# Download installer first
curl -fsSL https://raw.githubusercontent.com/aaron777collins/BetterPGVectorN8N/main/install.sh -o install.sh
chmod +x install.sh

# Then pick your method:
./install.sh --standalone   # New n8n + pgvector Docker setup
./install.sh --docker       # Add to existing Docker Compose
./install.sh --direct       # Install into running container
./install.sh --npm          # Install to ~/.n8n/nodes
./install.sh --update       # Update existing installation
```

Or via n8n UI: **Settings → Community Nodes → Install → `n8n-nodes-pgvector-advanced`**

</details>

<details>
<summary><b>Updating to latest version</b></summary>

```bash
# Update existing installation
./install.sh --update

# Or run the installer again - it auto-updates on container restart
docker compose restart n8n
```

The Docker init script automatically checks for updates on each container start.

</details>

---

## Why Use This?

| Built-in PGVector Node | This Package |
|------------------------|--------------|
| Insert only | Full CRUD (Upsert, Query, Delete, Get) |
| No stable IDs | External IDs for reliable syncing |
| Basic queries | Filters, pagination, multiple distance metrics |
| Single inserts | Batch operations (1000+ embeddings) |
| Manual schema | Auto table/index creation |
| No AI Agent tools | **AI Agent Tool for RAG workflows** |

---

## Quick Start

### 1. Set Up Credentials

In n8n: **Credentials → Add → Postgres**

```
Host: your-postgres-host
Port: 5432
Database: your_db
User: your_user
Password: your_password
```

### 2. Initialize Schema

Add a **PGVector Advanced** node with:
- Operation: `Admin`
- Admin Operation: `Ensure Schema`
- Dimensions: `1536` (or your embedding size)

### 3. Store Embeddings

```
Operation: Upsert
Collection: my_documents
External ID: doc-123
Content: "Your document text"
Embedding: [0.1, 0.2, 0.3, ...]
Metadata: {"category": "tech", "author": "Jane"}
```

### 4. Search

```
Operation: Query
Collection: my_documents
Query Embedding: [0.1, 0.2, ...]
Top K: 10
Distance Metric: cosine
```

---

## Operations

### Upsert (Insert/Update)

```json
{
  "operation": "upsert",
  "collection": "documents",
  "externalId": "doc-123",
  "content": "Document text",
  "metadata": {"category": "tech"},
  "embedding": [0.1, 0.2, ...]
}
```

**Batch mode:** Map fields from input items for bulk inserts.

### Query (Similarity Search)

```json
{
  "operation": "query",
  "collection": "documents",
  "queryEmbedding": [0.1, 0.2, ...],
  "topK": 10,
  "distanceMetric": "cosine",
  "metadataFilter": {"category": "tech"}
}
```

### Delete

```json
{
  "operation": "delete",
  "collection": "documents",
  "deleteBy": "externalId",
  "deleteExternalIds": "doc-1, doc-2"
}
```

Delete by: `id`, `externalId`, or `metadata` filter.

### Get

```json
{
  "operation": "get",
  "collection": "documents",
  "getBy": "externalId",
  "getExternalIds": "doc-1, doc-2"
}
```

### Admin

| Operation | What It Does |
|-----------|--------------|
| `ensureSchema` | Creates table + indexes if missing |
| `createIndex` | Adds HNSW or IVFFlat vector index |
| `dropCollection` | Deletes all records in a collection |

---

## Distance Metrics

| Metric | Best For |
|--------|----------|
| **Cosine** | Text embeddings (OpenAI, Cohere, etc.) |
| **L2** | When absolute distance matters |
| **Inner Product** | Pre-normalized vectors |

---

## Example Workflows

**Semantic Search:**
1. Parse documents → Generate embeddings (OpenAI) → Upsert to PGVector → Query similar

**Deduplication:**
1. Query existing → If similarity > threshold, skip → Else upsert

**Sync from External System:**
1. Use `externalId` to upsert → Automatically updates existing or inserts new

---

## Docker Persistence (How It Works)

The installer creates a custom Dockerfile that auto-installs community nodes on startup:

```
n8n/
├── Dockerfile        # Extends official n8n image
└── init-nodes.sh     # Installs packages on container start
```

To add more packages, edit `init-nodes.sh`:

```sh
PACKAGES="n8n-nodes-pgvector-advanced other-package"
```

Then: `docker compose build && docker compose up -d`

---

## Troubleshooting

**"pgvector extension not found"**
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

**Slow queries?**
- Create an HNSW index via Admin → Create Index
- Use metadata filters to reduce search space

**Dimension mismatch?**
- All embeddings in a collection must have the same dimensions
- Use different collections for different embedding models

---

## Development

```bash
git clone https://github.com/aaron777collins/BetterPGVectorN8N.git
cd BetterPGVectorN8N
npm install
npm run build
npm test
```

---

## AI Agent Tool

The **PGVector Store Tool** lets n8n AI Agents manage knowledge with natural operations:

| Operation | What it does |
|-----------|--------------|
| **Remember** | Store new info, update by ID or similar concept |
| **Recall** | Search with similarity threshold |
| **Forget** | Delete by exact ID |
| **Forget Similar** | Delete by concept (with dry-run safety) |
| **Lookup** | Get by exact ID |

### Configuration

Each operation has n8n settings (safety/behavior) and AI parameters (data):

| n8n Config | AI Provides |
|------------|-------------|
| Collection, thresholds, ID hints | Content, IDs, queries |
| Dry run mode, result limits | Metadata filters |

**Example - Remember operation:**
- n8n: `ID Format Hint = "meeting-YYYY-MM-DD"`, `Auto-Generate ID = ON`
- AI: `content`, `id` (optional), `metadata`

**Example - Forget Similar operation:**
- n8n: `Similarity Threshold = 0.8`, `Dry Run = ON`
- AI: `concept` (what to delete)

[Full AI Tools Documentation →](https://aaron777collins.github.io/BetterPGVectorN8N/ai-tools)

---

## MCP Server for External AI Agents

Use with Claude, GPT, or other AI agents outside n8n.

```bash
# Run directly
npx n8n-nodes-pgvector-advanced

# Or install globally
npm install -g n8n-nodes-pgvector-advanced
pgvector-mcp
```

**Available tools:** `pgvector_upsert`, `pgvector_query`, `pgvector_delete`, `pgvector_get`, `pgvector_admin`

Set environment variables: `PGHOST`, `PGPORT`, `PGDATABASE`, `PGUSER`, `PGPASSWORD`

[Full MCP Documentation →](https://aaron777collins.github.io/BetterPGVectorN8N/mcp)

---

## Documentation

| Guide | Description |
|-------|-------------|
| [Installation](https://aaron777collins.github.io/BetterPGVectorN8N/installation) | All installation methods |
| [Quick Start](https://aaron777collins.github.io/BetterPGVectorN8N/quick-start) | Get running in 5 minutes |
| [Operations](https://aaron777collins.github.io/BetterPGVectorN8N/operations) | Full operations reference |
| [AI Agent Tools](https://aaron777collins.github.io/BetterPGVectorN8N/ai-tools) | Use with n8n AI Agents |
| [MCP Server](https://aaron777collins.github.io/BetterPGVectorN8N/mcp) | Use with external AI (Claude) |
| [Docker Guide](https://aaron777collins.github.io/BetterPGVectorN8N/docker) | Persistent Docker setup |
| [Troubleshooting](https://aaron777collins.github.io/BetterPGVectorN8N/troubleshooting) | Common issues & fixes |

---

## License

MIT

---

**Made with ❤️ for the n8n community**

[View on GitHub](https://github.com/aaron777collins/BetterPGVectorN8N) | [npm](https://www.npmjs.com/package/n8n-nodes-pgvector-advanced) | [Full Docs](https://aaron777collins.github.io/BetterPGVectorN8N/)


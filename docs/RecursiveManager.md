# RecursiveManager

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/RecursiveManager)
- [GitHub Pages Site](http://www.aaroncollins.info/RecursiveManager/)
- [Latest Release: RecursiveManager v1.2.4 - Windows Support & Concurrency Fixes](https://github.com/aaron777collins/RecursiveManager/releases/tag/v1.2.4) (January 25, 2026)

## 📊 Project Details

- **Primary Language:** TypeScript
- **Languages Used:** TypeScript, HTML, Shell, JavaScript, CSS, Dockerfile
- **License:** MIT License
- **Created:** January 18, 2026
- **Last Updated:** January 28, 2026

## 📝 About

# RecursiveManager

> ⚠️ **NOT UNDER ACTIVE DEVELOPMENT**
>
> This project is no longer being actively maintained. CI/CD pipelines have been disabled.
> The code remains available for reference and archival purposes.
>
> *Last active: January 2026*

---

> Hierarchical AI agent system that mimics organizational structures for autonomous task management

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version: 1.2.4](https://img.shields.io/badge/Version-1.2.4-purple.svg)](https://github.com/aaron777collins/RecursiveManager/releases/tag/v1.2.4)
[![Status: Archived](https://img.shields.io/badge/Status-Archived-lightgrey.svg)](https://github.com/aaron777collins/RecursiveManager)

## Overview

RecursiveManager is a revolutionary AI agent orchestration system that models organizational hierarchies. Just as a CEO delegates to managers who delegate to workers, RecursiveManager enables AI agents to hire subordinates, manage tasks, escalate issues, and coordinate work across a recursive tree of specialized agents.

### Key Features

- **Recursive Agent Hierarchies**: Agents can hire and manage subordinates, creating organizational depth
- **Dual Instance Types**: Continuous execution for active work + reactive triggers for messages/events
- **File-Based Persistence**: Each agent has its own workspace with notes, tasks, and context
- **Multi-Framework Support**: Works with Claude Code, OpenCode, and other AI coding frameworks
- **Smart Scheduling**: Time-based triggers, continuous execution, and reactive messaging
- **Multi-Platform Integration**: Slack, Telegram, email, and internal messaging
- **Quality-First**: Multi-perspective analysis before all major decisions

### Philosophy

**Quality over cost.** RecursiveManager prioritizes correctness and thorough analysis over speed. Every major decision is analyzed from multiple perspectives (security, architecture, UX, etc.) to ensure robust outcomes.

**Stateless execution.** Every agent execution starts with a fresh memory context, reading all state from files. This prevents context window decay and enables truly long-running projects.

**Business-like structure.** Agents behave like employees in a company: they have roles, goals, managers, and subordinates. They hire, fire, escalate, and coordinate just like real organizations.

## Installation

### Quick Install (Recommended)

Install RecursiveManager with a single command:

```bash
curl -fsSL https://raw.githubusercontent.com/aaron777collins/RecursiveManager/master/scripts/install-binary.sh | bash
```

This downloads pre-built binaries, verifies checksums, and adds RecursiveManager to your PATH.

**[📖 Full Installation Guide](./INSTALL.md)** - Detailed instructions for all platforms

### Alternative Methods

**Manual Binary Install:**
1. Download from [Releases](https://github.com/aaron777collins/RecursiveManager/releases)
2. Extract: `tar xzf recursivemanager-v1.0.0-*.tar.gz -C ~/.recursivemanager`
3. Add to PATH: `export PATH="$HOME/.recursivemanager:$PATH"`

**From Source:**
```bash
git clone https://github.com/aaron777collins/RecursiveManager.git
cd RecursiveManager
npm install && npm run build && npm link
```

**CI/CD (Headless):**
```bash
VERSION=1.0.0 INSTALL_DIR=/opt/rm curl -fsSL https://raw.githubusercontent.com/aaron777collins/RecursiveManager/master/scripts/install-binary.sh | bash
```

## Quick Start

```bash
# Initialize with a high-level goal
recursivemanager init "Build a SaaS product for task management"

# The CEO agent will:
# 1. Analyze the goal from multiple perspectives
# 2. Create a strategic plan
# 3. Hire necessary team members (CTO, CMO, CFO, etc.)
# 4. Each hired agent further delegates as needed

# Monitor progress
recursivemanager status

# Output:
# ┌─ Organization Chart ─────────────────────────┐
# │ CEO                                          │
# │  ├─ CTO (Build the application)             │
# │  │  ├─ Backend Dev (API development)        │
# │  │  └─ Frontend Dev (UI development)        │
# │  ├─ CMO (Market the product)                │
# │  └─ CFO (Manage finances)                   │
# └──────────────────────────────────────────────┘
```

## Upgrading

Upgrade to the latest version:

```bash
recursivemanager-upgrade
```

Or upgrade to a specific version:

```bash
recursivemanager-upgrade 2.0.0
```

**[📖 Full Upgrade Guide](./UPGRADE.md)** - Upgrade, downgrade, rollback, and version management

## Documentation

- **[Installation Guide](./INSTALL.md)** - Complete installation instructions
- **[Upgrade Guide](./UPGRADE.md)** - Version management and upgrades
- **[API Documentation](./docs/API.md)** - Complete API reference
- **[Architecture](./docs/ARCHITECTURE.md)** - System design and internals
- **[Contributing](./CONTRIBUTING.md)** - How to contribute

## Updating (Legacy)

RecursiveManager includes a self-update mechanism:

```bash
# Check for updates
recursivemanager update --check

# Update to latest version
recursivemanager update

# Update to specific version
recursivemanager update 0.2.0

# Rollback to previous version
recursivemanager rollback

# View version history
recursivemanager update --history
```

## Documentation

📚 **[Full Documentation](https://aaron777collins.github.io/RecursiveManager/)** - Visit our comprehensive documentation website

### Quick Links

- **[Installation Guide](https://aaron777collins.github.io/RecursiveManager/installation/)** - Detailed installation instructions
- **[Quick Start](https://aaron777collins.github.io/RecursiveManager/quick-start/)** - Get started quickly
- **[Configuration](https://aaron777collins.github.io/RecursiveManager/configuration/)** - Configuration options
- **[CLI Reference](https://aaron777collins.github.io/RecursiveManager/cli-reference/)** - Command-line interface documentation
- **[API Reference](https://aaron777collins.github.io/RecursiveManager/api-reference/)** - API documentation
- **[Architecture](https://aaron777collins.github.io/RecursiveManager/architecture/overview/)** - System architecture

### Planning Documents

- **[COMPREHENSIVE_PLAN.md](./COMPREHENSIVE_PLAN.md)** - Complete system architecture and design
- **[MULTI_PERSPECTIVE_ANALYSIS.md](./MULTI_PERSPECTIVE_ANALYSIS.md)** - Analysis from 8 expert perspectives
- **[FILE_STRUCTURE_SPEC.md](./FILE_STRUCTURE_SPEC.md)** - Detailed file structure and schemas
- **[EDGE_CASES_AND_CONTINGENCIES.md](./EDGE_CASES_AND_CONTINGENCIES.md)** - Edge case handling
- **[IMPLEMENTATION_PHASES.md](./IMPLEMENTATION_PHASES.md)** - Phased implementation plan

### AI Provider & Integration Guides

- **[AI_PROVIDER_GUIDE.md](./docs/AI_PROVIDER_GUIDE.md)** - Complete guide to configuring AI providers
- **[AICEO_INTEGRATION_GUIDE.md](./docs/AICEO_INTEGRATION_GUIDE.md)** - Integration with AICEO Gateway for centralized LLM access

### CI/CD & DevOps

- **[JENKINS.md](./docs/JENKINS.md)** - Jenkins CI/CD pipeline setup and configuration

## AI Provider Configuration

RecursiveManager supports multiple AI providers with flexible configuration for both multi-perspective analysis and agent execution.

### Supported Providers

- **AICEO Gateway** (Recommended): Centralized rate-limited access with shared quota management across platforms
- **Direct Anthropic**: Direct API calls to Claude models
- **Direct OpenAI**: Direct API calls to GPT models
- **GLM Direct**: Direct API calls to GLM models
- **Custom Providers**: Support for custom LLM endpoints

### Quick Configuration

Configure your AI provider via environment variables:

```bash
# Use AICEO Gateway (recommended for shared quota management)
export AI_PROVIDER=aiceo-gateway
export AICEO_GATEWAY_URL=http://localhost:4000/api/glm/submit
export AICEO_GATEWAY_API_KEY=your-shared-secret
export AICEO_GATEWAY_PROVIDER=glm
export AICEO_GATEWAY_MODEL=glm-4.7

# Or use direct Anthropic
export AI_PROVIDER=anthropic-direct
export ANTHROPIC_API_KEY=sk-ant-...
export ANTHROPIC_MODEL=claude-sonnet-4-5

# Configure fallback provider
export AI_FALLBACK_PROVIDER=glm-direct
export GLM_API_KEY=your-glm-api-key
```

📖 **[Read the full AI Provider Guide](./docs/AI_PROVIDER_GUIDE.md)** for detailed configuration, provider comparison, and troubleshooting.

## Integration with AICEO

RecursiveManager integrates seamlessly with AICEO's GLM Gateway to enable:

- **Centralized Rate Limiting**: Shared quota management across all platforms (AICEO, RecursiveManager, Slack bots, etc.)
- **Priority Queue**: High/normal/low priority request handling
- **Cost Tracking**: Centralized LLM API cost monitoring and analytics
- **Automatic Failover**: Falls back to direct providers if gateway unavailable
- **Request Logging**: Full audit trail of all LLM requests

### Quick Integration

1. **Start AICEO Gateway**:
   ```bash
   cd /path/to/AICEO
   npm run dev
   ```

2. **Configure RecursiveManager**:
   ```bash
   export AI_PROVIDER=aiceo-gateway
   export AICEO_GATEWAY_URL=http://localhost:4000/api/glm/submit
   export AICEO_GATEWAY_API_KEY=your-shared-secret
   ```

3. **Test Integration**:
   ```bash
   recursivemanager analyze "Should we implement Redis caching?"
   ```

📖 **[Read the full AICEO Integration Guide](./docs/AICEO_INTEGRATION_GUIDE.md)** for step-by-step setup, testing, quota management, and monitoring.

### Core Concepts

#### Agent Hierarchy

Each agent has:
- **Identity**: Role, goal, capabilities
- **Manager**: Reports to another agent (except CEO)
- **Subordinates**: Can hire agents to delegate work
- **Workspace**: Personal directory for notes, tasks, research

#### Execution Modes

1. **Continuous**: Picks up next pending task, executes it, updates progress
2. **Reactive**: Triggered by messages (Slack, Telegram, manager, etc.)
3. **Scheduled**: Time-based triggers (daily standup, weekly review, etc.)

#### Task Management

- **Hierarchical**: Tasks can nest indefinitely (with depth limits)
- **Delegatable**: Tasks can be assigned to subordinate agents
- **Traceable**: Full audit trail of all task changes
- **Archivable**: Completed tasks archived to prevent clutter

#### Multi-Perspective Analysis

Before major decisions (hiring, firing, strategic changes), agents automatically trigger multi-perspective analysis using 8 specialized AI agents running in parallel:

**The 8 Perspectives:**
1. **Security**: Identifies risks, vulnerabilities, and compliance issues
2. **Architecture**: Analyzes scalability, maintainability, and technical debt
3. **Simplicity**: Advocates for YAGNI principle and reducing complexity
4. **Financial**: Evaluates costs, benefits, ROI, and resource utilization
5. **Marketing**: Assesses positioning, messaging, and competitive advantage
6. **UX**: Examines user experience, usability, and accessibility
7. **Growth**: Considers adoption, retention, and virality
8. **Emotional**: Evaluates team morale, user sentiment, and psychological impact

**Example Usage:**
```bash
# Manual analysis
recursivemanager analyze "Should we migrate to microservices?"

# Output: All 8 perspectives with confidence scores, synthesized decision
# ┌─────────────┬────────────┬────────────────────────────┐
# │ Perspective │ Confidence │ Summary                     │
# ├─────────────┼────────────┼────────────────────────────┤
# │ Security    │ 0.85       │ Increases attack surface... │
# │ Architecture│ 0.82       │ Better scalability but...   │
# │ ...         │ ...        │ ...                         │
# └─────────────┴────────────┴────────────────────────────┘
```

Results are synthesized into a decision with overall confidence levels (accounting for agreement/disagreement between perspectives) and full reasoning. All analyses are cached and persisted to agent workspaces for audit trails.

**Automatic Triggers:**
- Before hiring a new agent
- Before firing an agent
- Before major configuration changes
- On-demand via CLI command

## Architecture

```
┌─────────────────────────────────────────┐
│           CLI Tool                      │
│  (User-facing interface)                │
└───────────┬─────────────────────────────┘
            │
┌───────────▼─────────────────────────────┐
│      Scheduler Daemon                   │
│  (Time-based + event triggers)          │
└───────────┬─────────────────────────────┘
            │
┌───────────▼─────────────────────────────┐
│    Core Orchestrator                    │
│  (Framework-agnostic execution)         │
└─┬─────────┬─────────────┬───────────────┘
  │         │             │
┌─▼──────┐ ┌▼──────────┐ ┌▼─────────────┐
│ Claude │ │ OpenCode  │ │ Future       │
│ Code   │ │           │ │ Adapters     │
└────────┘ └───────────┘ └──────────────┘

┌─────────────────────────────────────────┐
│   Messaging Integration Layer           │
│  ┌────────┐ ┌────────┐ ┌────────┐      │
│  │ Slack  │ │Telegram│ │ Email  │      │
│  └────────┘ └────────┘ └────────┘      │
└─────────────────────────────────────────┘

            ▼

┌─────────────────────────────────────────┐
│     File-Based State Storage            │
│  agents/{shard}/{agent-id}/             │
│    ├── config.json                      │
│    ├── schedule.json                    │
│    ├── tasks/                           │
│    ├── inbox/                           │
│    └── workspace/                       │
└─────────────────────────────────────────┘
```

## Project Status

**Current Phase**: Production Release (v1.0.0)

RecursiveManager is now **PRODUCTION READY** with all core phases complete. The system has undergone comprehensive testing, security hardening, and production deployment preparation.

### Production-Ready Features (v1.0.0)

✅ **Core System**
- Recursive agent hierarchy with manager-subordinate relationships
- File-based persistence with agent workspaces
- Multi-perspective analysis with real AI provider integration (8 perspectives)
- Decision synthesis with confidence levels and conflict detection
- Agent locking mechanisms using async-mutex
- ExecutionPool with worker pool pattern (configurable concurrency)
- PID file management for process tracking
- **Test Coverage**: 2337/2337 tests passing (100% pass rate)

✅ **Multi-Provider AI Integration**
- AICEO Gateway support (centralized rate limiting and quota management)
- Direct Anthropic API integration (Claude models)
- Direct OpenAI API integration (GPT models)
- GLM Direct API support
- Custom provider endpoints
- Automatic failover to backup providers
- Per-request provider override capability

✅ **Advanced Task Execution**
- **Priority Queue System**: Task priorities (low, medium, high, urgent)
- **Dependency Management**: Task dependency graph with cycle detection
- **Resource Quotas**: CPU, memory, and time limits per agent
- **Execution Modes**: Continuous, reactive (message-triggered), scheduled (cron)
- **Worker Pool**: Configurable max concurrent executions (default: 10)
- **Queue Metrics**: Wait time tracking and queue depth monitoring

✅ **Security Hardening**
- **Database Encryption**: AES-256-GCM authenticated encryption at rest
- **Secret Management**: Encrypted storage for API keys with audit logging
- **Secret Rotation**: Manual/automatic rotation policies with expiration tracking
- **Audit Logging**: Comprehensive security event tracking
- **Input Validation**: Request size limits and sanitization
- **Dependency Scanning**: Automated vulnerability scanning in CI/CD
- **OWASP Coverage**: Security tests for Top 10 vulnerabilities

✅ **Snapshot & Disaster Recovery**
- Automatic snapshots on agent hire/fire operations
- Manual snapshot creation via CLI
- Snapshot validation and integrity checking
- Interactive rollback with snapshot selection
- Backup creation before restoration
- Metadata tracking (ID, reason, timestamp, size, schema version)

✅ **Monitoring & Observability**
- **Prometheus Metrics**: 15+ metrics covering executions, queues, agents, resources
- **Grafana Dashboards**: 3 pre-built dashboards (Overview, Agent Performance, System Metrics)
- **Alerting Rules**: 13 comprehensive alert rules (error rates, resource usage, queue backlog, etc.)
- **Structured Logging**: JSON format with Winston, automatic rotation and compression
- **Correlation IDs**: Distributed tracing with trace IDs across all operations
- **Log Levels**: Configurable via environment variable (debug, info, warn, error)
- **CLI Metrics Server**: `recursivemanager metrics` command with `/health` and `/metrics` endpoints

✅ **Docker Production Deployment**
- Multi-stage production Dockerfile (security scanning with Trivy)
- Non-root user execution (UID 1001)
- Docker Compose stack with Prometheus + Grafana
- Health checks and automatic restarts
- Volume management for data persistence
- Resource limits (configurable CPU/memory)
- Signal handling with dumb-init

✅ **CLI Interface** (13 Commands)
- `recursivemanager init` - Initialize with goal
- `recursivemanager status` - Show org chart and agent details
- `recursivemanager hire` - Hire new agents (with multi-perspective analysis)
- `recursivemanager fire` - Fire agents (with automatic snapshot)
- `recursivemanager message` - Send messages to agents for reactive execution
- `recursivemanager run` - Manually trigger agent execution
- `recursivemanager logs` - View and filter agent logs with advanced search
- `recursivemanager analyze` - Run multi-perspective AI analysis
- `recursivemanager metrics` - Start Prometheus metrics HTTP server
- `recursivemanager update` - Self-update system with rollback
- `recursivemanager config` - Configuration management
- `recursivemanager debug` - Agent debugging and inspection
- `recursivemanager rollback` - Restore from database snapshots

📖 **[Complete CLI Reference](./docs/cli-reference.md)** - Full documentation for all commands

✅ **Installation & Updates**
- One-liner installation script with headless mode
- Binary distribution for multiple platforms
- Self-update mechanism via GitHub API
- Version rollback capability
- Version history tracking

✅ **Documentation**
- Comprehensive website with VitePress
- Architecture documentation with system diagrams
- API reference documentation
- CLI reference with examples
- Development and contribution guides
- Monitoring and security guides

✅ **CI/CD & Testing**
- GitHub Actions workflows for CI, release, and docs
- Automated testing across Node.js 18, 20, 22
- Code coverage reporting with Codecov
- Turbo monorepo orchestration
- Automated dependency vulnerability scanning
- Release automation on version tags

### Phase Completion Status

- ✅ **Phase 1**: Testing & Build Verification (2337/2337 tests passing)
- ✅ **Phase 2**: Multi-Perspective AI Analysis (Real provider integration complete)
- ✅ **Phase 3**: CLI Commands (All 13 commands implemented)
- ✅ **Phase 4**: Scheduler Enhancements (Priority queue, dependencies, resource quotas)
- ✅ **Phase 5**: Snapshot System (Full backup/restore with validation)
- ✅ **Phase 6**: Security Hardening (Encryption, secrets, audit logging)
- ⚠️ **Phase 7**: Jenkins CI/CD (GitHub Actions active, Jenkins setup blocked)
- ✅ **Phase 8**: Docker Production Deployment (Multi-stage build, compose stack)
- ✅ **Phase 9**: Monitoring & Metrics (Prometheus, Grafana, alerting)
- 🔄 **Phase 10**: Documentation (In progress - core docs complete)
- ⏸️ **Phase 11**: Binary Distribution (Planned)
- ⏸️ **Phase 12**: Post-Launch Verification (Planned)

### Upcoming Features

See [IMPLEMENTATION_PHASES.md](./IMPLEMENTATION_PHASES.md) for the full roadmap.

## Design Principles

### Complexity Management

RecursiveManager is inherently complex (recursive hierarchies, multi-framework support, distributed state). We manage this complexity through:

1. **Progressive Disclosure**: Simple by default, powerful when needed
2. **Clear Abstractions**: Hide implementation details behind clean interfaces
3. **Excellent Documentation**: Every feature explained with examples
4. **Smart Defaults**: Works out-of-box for common use cases
5. **Actionable Errors**: Error messages include suggested fixes
6. **Debugging Tools**: Single-command insights into system state

### Developer Experience

- **One-command start**: `recursivemanager init "goal"`
- **Convention over configuration**: Sensible defaults everywhere
- **Self-documenting**: Files include README.md and comments
- **Fail fast**: Validate early, fail with clear messages
- **Easy debugging**: `recursivemanager debug <agent-id>` shows everything

### Testing Strategy

- **Unit Tests**: 80%+ coverage, fast feedback
- **Integration Tests**: Component interactions validated
- **E2E Tests**: Full user journeys tested
- **Performance Tests**: Scalability to 1000+ agents
- **Edge Case Tests**: Every contingency tested

See [Edge Cases document](./EDGE_CASES_AND_CONTINGENCIES.md) for comprehensive edge case catalog.

## Use Cases

### Software Development

```bash
# CEO hires CTO
# CTO hires Backend Dev, Frontend Dev, DevOps
# Each dev implements their piece
# CTO coordinates integration
# CEO reviews final product
```

### Content Creation

```bash
# CEO hires Content Strategist
# Strategist hires Writers, Editors, SEO Specialist
# Writers create content
# Editors review
# SEO optimizes
# Strategist publishes
```

### Data Analysis

```bash
# CEO hires Data Scientist
# Data Scientist hires Data Engineer, ML Engineer
# Data Engineer builds pipeline
# ML Engineer trains models
# Data Scientist synthesizes insights
```

### Customer Support

```bash
# CEO hires Support Manager
# Support Manager monitors Slack/Email
# Escalates to specialists as needed
# Specialists resolve issues
# Support Manager follows up
```

## Community

### Contributing

We welcome contributions! See our [Contributing Guide](https://aaron777collins.github.io/RecursiveManager/development/contributing/) for details.

**Ways to Contribute:**
- Report bugs or suggest features via [GitHub Issues](https://github.com/aaron777collins/RecursiveManager/issues)
- Improve documentation
- Submit pull requests for bug fixes or features
- Share use cases and examples
- Help test edge cases

### Support & Discussion

- **GitHub Issues**: [Report bugs or request features](https://github.com/aaron777collins/RecursiveManager/issues)
- **GitHub Discussions**: [Ask questions and share ideas](https://github.com/aaron777collins/RecursiveManager/discussions)
- **Documentation**: [Full documentation site](https://aaron777collins.github.io/RecursiveManager/)

## License

MIT License - see [LICENSE](./LICENSE) for details

## Acknowledgments

This project is inspired by:
- **Ralph**: The autonomous development loop concept
- **AICEO**: The multi-agent analysis approach
- **Real organizations**: How businesses actually delegate and coordinate

## Contact

- **GitHub**: [RecursiveManager](https://github.com/aaron777collins/RecursiveManager)
- **Issues**: [Report bugs or request features](https://github.com/aaron777collins/RecursiveManager/issues)
- **Documentation**: [https://aaron777collins.github.io/RecursiveManager/](https://aaron777collins.github.io/RecursiveManager/)

---

**Version**: 1.0.0 (Production)
**Status**: Production Ready - comprehensive testing, security hardening, monitoring, and deployment complete
**Philosophy**: Quality over cost. Multi-perspective analysis. Stateless execution. Business-like structure.
**Goal**: Enable AI agents to coordinate like real organizations, handling complex, long-running projects autonomously.


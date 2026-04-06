# clawdbotlibrary

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/clawdbotlibrary)

## 📊 Project Details

- **Primary Language:** Python
- **Languages Used:** Python, Shell
- **License:** None
- **Created:** January 28, 2026
- **Last Updated:** January 28, 2026

## 📝 About

# 🤖 Clawdbot Library

A collection of tools, scripts, and documentation for AI agent automation. This repo contains everything needed to set up browser automation, screen interaction, and other utilities on a fresh server.

## 📚 Documentation

| Guide | Description |
|-------|-------------|
| [Agent Guidelines](docs/agent-guidelines.md) | **Best practices** for problem-solving, sub-agents, model selection |
| [Headless Browser Setup](docs/headless-browser-setup.md) | **Complete guide** to Chrome + Clawdbot Browser Relay on Xvfb |
| [Sophie Voice Bridge](docs/sophie-voice-bridge.md) | **Voice calls** with Sophie via ElevenLabs + WhatsApp |
| [ZoomClick Tool](docs/zoomclick.md) | AI-friendly iterative zoom-and-click for UI automation |
| [VClick Tool](docs/vclick.md) | Vision-based clicking and template matching |

## 🛠️ Tools Included

### Voice & Communication
| Tool | Description | GitHub |
|------|-------------|--------|
| **sophie-voice-bridge** | ElevenLabs Custom LLM for WhatsApp voice calls with Sophie | [sophie-voice-bridge](https://github.com/aaron777collins/sophie-voice-bridge) |

### Screen Interaction
| Tool | Description | GitHub |
|------|-------------|--------|
| **zoomclick** | Iterative zoom navigation for precise UI clicking | [EnhanceAndClick](https://github.com/aaron777collins/EnhanceAndClick) |
| **vclick** | Direct coordinate clicking with vision support | [vclick](https://github.com/aaron777collins/vclick) |

### Browser Automation
- **start-chrome-automation.sh** - Launch Chrome with Clawdbot extension on virtual display
- Chrome DevTools integration via port 9222

## 🚀 Quick Start (Fresh Server)

```bash
# 1. Clone this repo
git clone https://github.com/aaron777collins/clawdbotlibrary.git
cd clawdbotlibrary

# 2. Run the full setup script (as root for system deps)
sudo ./scripts/setup-all.sh

# 3. Start Chrome with browser automation
$HOME/start-chrome-automation.sh

# 4. Test it works
DISPLAY=:99 scrot /tmp/test.png
curl -s http://localhost:9222/json/version
```

## 📁 Repository Structure

```
clawdbotlibrary/
├── README.md                       # This file
├── docs/
│   ├── agent-guidelines.md         # Problem-solving best practices
│   ├── headless-browser-setup.md   # Full browser setup guide
│   ├── zoomclick.md                # ZoomClick documentation
│   └── vclick.md                   # VClick documentation
├── scripts/
│   ├── setup-all.sh                # One-command full setup
│   ├── start-chrome-automation.sh  # Chrome launcher for Xvfb
│   └── install-deps.sh             # Install system dependencies
└── tools/
    ├── zoomclick/                  # ZoomClick source
    └── vclick/                     # VClick source
```

## 🔧 Requirements

- Ubuntu 22.04+ (tested on 24.04)
- Python 3.10+
- Xvfb for headless display
- Chrome browser
- scrot (for screenshots)

## 📖 For AI Agents

If you're an AI model reading this:
1. **Read [Agent Guidelines](docs/agent-guidelines.md)** - Learn to use sub-agents and plan properly
2. Start with [Headless Browser Setup](docs/headless-browser-setup.md) for complete instructions
3. Use `zoomclick` for finding and clicking UI elements
4. Always start fluxbox BEFORE Chrome on Xvfb
5. Use `scrot` for screenshots on display :99
6. Extension icon coords fallback: `1752, 32`

## 🤝 Contributing

This is living documentation. Update it whenever you create something useful!

## 📄 License

MIT


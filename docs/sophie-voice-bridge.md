# sophie-voice-bridge

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/sophie-voice-bridge)

## 📊 Project Details

- **Primary Language:** Python
- **Languages Used:** Python, Dockerfile
- **License:** None
- **Created:** January 28, 2026
- **Last Updated:** January 28, 2026

## 📝 About

# Sophie Voice Bridge

ElevenLabs Custom LLM server that connects to Sophie AI via Clawdbot.

## Architecture

```
WhatsApp Call → ElevenLabs (STT/TTS) → Haiku (fast) ─┬─→ Direct response
                                                      │
                                                      └─→ ask_sophie → Sophie/Opus
                                                                          (full capabilities)
```

- **Haiku** handles fast voice responses (1-3 sentences)
- **ask_sophie tool** escalates complex questions to Sophie (Opus with tools)
- Sophie has access to calendar, email, web search, files, memory, etc.

## Quick Start (Docker)

```bash
# Clone
git clone https://github.com/aaron777collins/sophie-voice-bridge.git
cd sophie-voice-bridge

# Configure
cp .env.example .env
# Edit .env with your Clawdbot gateway token

# Run
docker compose up -d

# Check health
curl http://localhost:8013/health
```

## Configuration

Create `.env` file:

```env
CLAWDBOT_GATEWAY_URL=http://localhost:18789
CLAWDBOT_GATEWAY_TOKEN=your-gateway-token
```

## API Endpoints

Both routes work (ElevenLabs uses `/chat/completions`):

```
POST /v1/chat/completions    # OpenAI standard
POST /chat/completions       # ElevenLabs format
GET  /health                 # Health check
```

---

## 🎙️ ElevenLabs Setup Guide

### Step 1: Create an Agent

1. Go to [ElevenLabs Agents Platform](https://elevenlabs.io/app/agents)
2. Click **"Create Agent"**
3. Give it a name (e.g., "Sophie Voice")

### Step 2: Configure LLM (Custom)

1. In Agent settings, go to **"LLM"** section
2. Select **"Custom LLM"**
3. Configure:
   - **Server URL:** `https://voice.aaroncollins.info`
   - **Model:** `haiku` (or anything - it's ignored)
   - **Custom LLM extra body:** ✅ Enable this
   - **Limit token usage:** `5000` (recommended)

### Step 3: Configure Voice

1. Go to **"Voice"** section
2. Choose a voice you like (the voice Sophie will speak with)
3. Adjust stability/clarity as needed

### Step 4: Connect WhatsApp (via Twilio)

1. Go to **"Phone Numbers"** section
2. Click **"Import Phone Number"**
3. Enter your Twilio credentials:
   - **Phone Number:** Your Twilio number with WhatsApp enabled
   - **Twilio SID:** From Twilio console
   - **Twilio Token:** From Twilio console
4. **Assign the agent** to the phone number

### Step 5: Test

**Outbound call (you call someone):**
1. In Phone Numbers, click the outbound call button
2. Select your agent
3. Enter the phone number to call
4. Click "Send Test Call"

**Inbound call (someone calls you):**
- Call your Twilio number on WhatsApp
- The agent will answer automatically

---

## How It Works

1. **You speak** on WhatsApp call
2. **ElevenLabs STT** transcribes your speech to text
3. **Text sent** to `/chat/completions` endpoint
4. **Haiku evaluates:**
   - Simple question → responds directly (fast, 1-3 sentences)
   - Complex question → uses `ask_sophie` tool
5. **If ask_sophie used:**
   - Sophie (Opus) processes with full tool access
   - Can check calendar, email, search web, access files
   - Haiku relays response conversationally
6. **ElevenLabs TTS** converts response to speech
7. **You hear** Sophie's voice response

## When ask_sophie is Used

Haiku automatically escalates to Sophie when you ask about:
- Calendar, schedule, events, appointments
- Emails, messages, notifications
- Files, documents, code, projects
- Research requiring web search or browsing
- Complex technical or business questions
- Anything requiring memory of past conversations

Simple greetings, math, and general knowledge are handled by Haiku directly.

---

## Development

```bash
# Local setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run locally
python bridge.py
```

## Test Commands

```bash
# Health check
curl https://voice.aaroncollins.info/health

# Simple question (Haiku direct)
curl -X POST https://voice.aaroncollins.info/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "What is 2+2?"}], "stream": false}'

# Complex question (triggers ask_sophie)
curl -X POST https://voice.aaroncollins.info/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "What meetings do I have tomorrow?"}], "stream": false}'
```

## License

MIT


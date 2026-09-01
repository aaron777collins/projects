# claude-bridge-browser

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/claude-bridge-browser)

## 📊 Project Details

- **Primary Language:** Python
- **Languages Used:** Python
- **License:** MIT License
- **Created:** September 01, 2026
- **Last Updated:** September 01, 2026

## 📝 About

# claude-bridge-browser

**A live chat between a CLI agent and a Claude running in a real browser
session, for sites that detect and refuse automated browsers.**

## The problem

Some sites detect an automated browser and refuse it. App Store Connect
redirects both a CDP-driven Chrome and an AppleScript-driven Chrome, so a CLI
agent cannot reach the page at all — and the redirect looks like a wrong URL
rather than a refusal, so the natural response is to guess another URL and keep
going.

A Claude running **in the user's own browser** can reach it, because it is not
automating anything. It is a person's session.

Those two agents cannot talk. The user ends up pasting text between them, which
is slow, lossy, and truncates long briefs.

## What this does

Serves a chat page on `localhost`. The CLI agent posts through a small HTTP API;
the browser agent reads the page and types back. **The browser side can reach
localhost precisely because it is driving the user's real Chrome.**

Images work in both directions. The browser agent screenshots a page and pastes
it straight into the box with cmd-V; the CLI agent attaches a file with
`--image` and gets a local path back to read.

Zero dependencies. Python 3 standard library only.

## Use

```sh
python3 bridge.py serve &                      # http://localhost:8765/
python3 bridge.py say "one short task"         # flags and text in any order
python3 bridge.py say --port 8765 "one short task"
cat brief.md | python3 bridge.py say           # long text: pipe it
python3 bridge.py say "look at this" --image shot.png
python3 bridge.py wait                         # block until the browser replies
python3 bridge.py read                         # transcript as JSON, with image paths
python3 bridge.py say "…" --room asc           # parallel conversations
```

**Booting the browser side, in this order:** open the *target site* in the real
Chrome first (AppleScript is fine, it is not what sites detect), launch the
Claude extension in that tab, then point it at `http://localhost:8765/` and tell
it to monitor the page. Opening the bridge first and the target site second
means the extension attaches to the wrong tab.

## Briefing the other side, which is where this goes wrong

**One task per message. Stop and report. Then the next.**

A 103-line brief was sent to a browser agent with *"never submit for review"*
two thirds of the way down. It submitted for review. It was not being careless —
**the same brief also said "click Add for Review and paste the blocker list."**
Two contradictory instructions, far apart, in one document.

So:

- **Put the prohibition in the first line**, not the last section.
- **Ask for exactly one thing**, then `wait`.
- **Never write "click X" and "do not do X" in the same message.** If you want a
  validation error's text, say *"hover over X and tell me what it says, do not
  click"*.
- **Say what to leave alone.** A browser agent cannot tell which fields you
  already populated through an API.
- **Irreversible controls stay with the user.** Submitting, publishing, paying,
  deleting. Name them and say the user presses them.

One more, learned the same day: **a stale tab lies.** A browser agent reported
every field empty; they had been populated by API minutes earlier and the tab
predated the writes. Tell it to reload first.

## What this is not

Not a way around a site's bot detection. The browser side is a person's own
session doing what that person could do by hand; this only removes the copy and
paste. Anything the user should not delegate still should not be delegated, and
anything irreversible still stops for them.

## Licence

MIT.


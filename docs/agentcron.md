# agentcron

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/agentcron)

## 📊 Project Details

- **Primary Language:** Rust
- **Languages Used:** Rust, PowerShell, Shell
- **License:** MIT License
- **Created:** August 10, 2026
- **Last Updated:** August 10, 2026

## 📝 About

# agentcron

Schedule prompts to run headlessly through `claude`, `codex`, or any CLI you like — on your OS's real scheduler, managed from a terminal UI.

## Install

**Linux / macOS**

```sh
curl -fsSL https://raw.githubusercontent.com/aaron777collins/agentcron/main/install.sh | sh
```

**Windows (PowerShell)**

```powershell
irm https://raw.githubusercontent.com/aaron777collins/agentcron/main/install.ps1 | iex
```

Both installers build from source, so they need the [Rust toolchain](https://rustup.rs). They install to `~/.local/bin` (Linux/macOS) or `%LOCALAPPDATA%\agentcron\bin` (Windows), create the data directories, and put the install directory on your `PATH`. They are idempotent — re-run either one to upgrade.

## Usage

Run `agentcron` with no arguments for the TUI.

**Job list**

| Key | Action |
| --- | --- |
| `n` | New job |
| `e` | Edit job |
| `d` | Delete job (asks first) |
| `space` | Enable / disable |
| `r` | Run now |
| `l` | History and logs |
| `/` | Filter |
| `q` | Quit |

**Job editor** — `Enter` on the prompt field opens it in `$EDITOR`/`$VISUAL` (same tempfile round-trip as `git commit`), `Ctrl+S` saves, `Esc` cancels. Schedules are picked from contextual fields — once, daily, weekly, or every N minutes/hours. There is no cron syntax to write.

Each job has an executor: `claude -p`, `codex exec`, or a custom template where `{prompt}` is substituted. The two built-in executors are fed the prompt on stdin rather than as an argument, which is what lets a multi-line prompt work against the `.cmd` shims npm installs on Windows.

A run is killed if it exceeds 30 minutes, and recorded with exit code `124`.

There is also a headless entry point:

```sh
agentcron run <job-id>
```

That is what the OS scheduler invokes at the scheduled time. You would not normally run it by hand — use `r` in the TUI to run a job immediately and watch its output live.

## How scheduling works

agentcron does not run a background daemon. It registers each job with the scheduler your OS already has: Task Scheduler on Windows (per-user tasks under an `agentcron\` folder), a marker-delimited block in your crontab on Linux, and a launchd agent per job on macOS. Each registration just tells the OS to run `agentcron run <job-id>` at the right times.

The payoff is that jobs survive reboots and there is no extra process to babysit or keep alive — if your machine is on, your jobs fire. If a scheduler registration ever fails, the job is still saved locally and flagged in the job list, so a bad `schtasks`/`crontab`/`launchctl` call never loses your config.

Windows tasks run only while you are logged in, which is a known v1 limitation.

## Building from source

```sh
git clone https://github.com/aaron777collins/agentcron.git
cd agentcron
cargo build --release
```

The binary lands at `target/release/agentcron`. Copy it anywhere on your `PATH`.

Jobs and logs live in the OS application data directory: `~/.local/share/agentcron` on Linux, `~/Library/Application Support/agentcron` on macOS, and `%APPDATA%\agentcron\data` on Windows.

## License

MIT — see [LICENSE](LICENSE).


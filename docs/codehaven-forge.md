# codehaven-forge

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/codehaven-forge)

## 📊 Project Details

- **Primary Language:** Rust
- **Languages Used:** Rust, HTML, Shell, Python, CSS, JavaScript, Dockerfile, Makefile
- **License:** MIT License
- **Created:** November 22, 2026
- **Last Updated:** November 22, 2026

## 📝 About

# Codehaven

A self-hosted code forge written in Rust. It hosts git over HTTP and SSH and has issues, pull
requests with review, CI with registered runners, releases, packages and a container registry.

It is made to be run by anyone. There is no sign-up page: the first account is made on the
server with one command, and every account after it comes from an invite. Nothing is readable
without signing in.

## Quick start

You need a Linux machine with Docker (Compose 2.24 or newer, and buildx), git, openssl, curl,
python3 and iproute2, 4 GB of memory and 20 GB of free disk. You do not need Rust or PostgreSQL
on the host. Everything builds and runs in containers.

```sh
git clone <repository-url> codehaven && cd codehaven
cp .env.example .env                      # set the URL, the paths and the proxy
sudo bash deploy/prod/setup.sh            # checks the host, makes the directories and secrets
sudo bash deploy/prod/up.sh               # builds the images and starts the instance
sudo bash deploy/prod/first-admin.sh <username> <email>
```

`first-admin.sh` prints a link that works once, for one hour. Open it, choose a password and turn
on two-factor sign-in. The script refuses to run when any account exists, and it never deletes
one.

The first build compiles the server, so it takes a while. Setup generates the database password
once and never prints it, and the server makes its own master key on first start.

### What goes in `.env`

`.env.example` lists every setting with a comment. A setting that is missing stops the scripts
with its name; nothing falls back to a guess. The ones you must choose:

| Setting | What it is |
| --- | --- |
| `CODEHAVEN_EXTERNAL_URL` | The address people open, for example `https://code.example.com` |
| `CODEHAVEN_DATA_DIR`, `CODEHAVEN_SECRETS_DIR`, `CODEHAVEN_BACKUP_DIR` | Where data, database credentials and backups live. Backups must be outside the checkout |
| `CODEHAVEN_PROXY` | How people reach the server: `none`, `network` or `caddy` (below) |
| `CODEHAVEN_TRUSTED_PROXIES` | A JSON list of the networks your proxy reaches the server from. `[]` when nothing sits in front |

### Putting it on the internet

Codehaven speaks plain HTTP and expects a proxy to add TLS.

- `CODEHAVEN_PROXY=none` publishes the web server and ssh on loopback only. Use it to try
  Codehaven on one machine, or behind a proxy that runs on the host.
- `CODEHAVEN_PROXY=network` joins the server to a Docker network where your own proxy already
  runs. Set `CODEHAVEN_PROXY_NETWORK` and `CODEHAVEN_PROXY_ALIAS`, then point a site at
  `<alias>:3200`.
- `CODEHAVEN_PROXY=caddy` starts a Caddy that gets the certificate for `CODEHAVEN_SITE_HOST` on
  its own. The name must already point at the machine, and ports 80 and 443 must be free. Set
  `CODEHAVEN_EDGE_SUBNET` and put it in `CODEHAVEN_TRUSTED_PROXIES`. The setup is in
  `deploy/Caddyfile.example`.

Whatever you use, send every path to the server, remove any `Remote-User` style header a client
sends, and do not buffer responses. Codehaven reads no identity header, so a proxy cannot sign
anyone in by accident. After it is up, check it from outside:

```sh
bash deploy/dev/public-smoke.sh https://code.example.com
```

## Everyday tasks

| Task | How |
| --- | --- |
| Invite someone | Site admin, then Invites. Or `deploy/compose.sh exec server codehaven admin invite create --email bob@example.com` |
| Run CI | Register a runner, then start it: `HAVEN_RUNNER_TOKEN=<token> sudo -E bash deploy/prod/ci-up.sh register runner-1`, then `sudo bash deploy/prod/ci-up.sh` |
| Back up | `sudo bash deploy/prod/backup.sh` |
| Restore | `sudo bash deploy/prod/restore.sh <archive>`, into an empty location |
| Upgrade | Back up, `git pull`, then `sudo bash deploy/prod/up.sh` |
| See the state | `deploy/compose.sh ps`, `deploy/compose.sh logs server` |
| Connect Claude | Set `CODEHAVEN_MCP_ENABLED=true`, run `up.sh` again, then add `https://<your address>/mcp` as a connector (see `docs/connector.md`) |

`docs/operations.md` covers backup, restore, upgrade and rollback in full. `docs/integration.md`
walks the first run and the runner.

## The browser workspace

Codehaven now has a workspace for each repository at `/{owner}/{repo}/workspace`. These parts
are live:

- **Editor.** Monaco, the editor inside VS Code, with a file tree, tabs, search and a diff.
  Unsaved edits are kept as drafts in the browser, encrypted, and locked when you sign out.
- **Commit.** Many files in one commit, to the current branch or a new one, with a pull request
  link when you commit to a new branch.
- **Runs.** The workflows of each commit and their live logs beside the code, with run, re-run
  and cancel.

It is for signed-in accounts only. Nobody who is signed out can open any workspace page, file or
stream, even for a public repository. A signed-in account sees the workspace of a repository it
can read, and needs write access to commit or run. The server starts no shell and no container
for it, and the editor is served by the instance itself, with nothing loaded from another site.

The terminal, a shell that runs in your browser, is still being built. The workspace code comes
to this repository with the next source update.

## Building and testing

Builds and tests run in a container, on this machine or on another host over ssh. Set `CH_HOST`
and `CH_REMOTE_ROOT` (in the environment, or in the untracked `deploy/dev/local.env`) to build
over ssh. With neither set, nothing ever contacts another machine.

```sh
make test [P=ch-core]     # tests, the whole workspace or one crate
make ci                   # the gate: the portability check, formatting, clippy, build, tests
make e2e E2E_TAG=test-x   # a full stack in a throwaway project, torn down after
```

`make ci` also runs `deploy/check-portable.py`, which fails when the name, address or path of a
particular server gets into the tree. Test stacks use a project name and an image tag that must
be throwaway names, and refuse any stack that already holds an account.

## Documents

- `ARCHITECTURE.md`: the design and the decisions behind it.
- `ROADMAP.md`: the build plan and the end-to-end test.
- `docs/`: one page per area (`foundation`, `identity`, `git`, `web`, `collab`, `ci`, `runner`,
  `integration`), `operations` and `connector` (connecting Claude).


# codehaven-forge

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/codehaven-forge)

## 📊 Project Details

- **Primary Language:** Rust
- **Languages Used:** Rust, JavaScript, HTML, Shell, Python, CSS, PLpgSQL, Dockerfile, Makefile
- **License:** MIT License
- **Created:** November 22, 2026
- **Last Updated:** November 22, 2026

## 📝 About

# Codehaven

A self-hosted code forge written in Rust. It hosts git over HTTP and SSH and has issues, pull
requests with review, CI with registered runners, releases, packages and a container registry.

It is made to be run by anyone. There is no sign-up page: the first account is made on the
server with one command, and every account after it comes from an invite. A repository starts
private; its owner can widen it to every signed-in account on the server, or to anyone on the
internet while the site admin allows public repositories.

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

Every repository has a workspace at `/{owner}/{repo}/workspace`, opened from the repository page.
It has four parts, and all four are live:

- **Editor.** Monaco, the editor inside VS Code, with a file tree, tabs, search and a diff.
  Unsaved edits are kept as drafts in the browser, encrypted, and locked when you sign out.
- **Commit.** Many files in one commit, to the current branch or a new one, with a pull request
  link when you commit to a new branch.
- **Runs.** The workflows of each commit and their live logs beside the code, with run, re-run
  and cancel.
- **Terminal.** A bash shell with pipes, loops, grep, sed, awk, find, sort, diff and jq, on a copy
  of the repository's files with your drafts on top. It runs in your browser, with no internet,
  and nothing it changes reaches your drafts until you tick it in review.

It is for signed-in accounts only. Nobody who is signed out can open any workspace page, file or
stream, even for a public repository. A signed-in account sees the workspace of a repository it
can read, and needs write access to commit or run. Streams close as soon as access ends. The
server starts no shell and no container for it, and every file the editor needs is served by the
instance itself, with nothing loaded from another site.

A site admin with two-factor sign-in can turn the editor off at `/admin/workspace`. The terminal
is on by default and can be turned off there separately from the editor.

## Pages

A repository can publish a static site from a branch, from its root or its `docs` folder, like
GitHub Pages. Every push to that branch publishes a new copy; a failed copy says why and the last
good one keeps serving, and an older copy can be put back. Turn it on in the repository's
Settings > Pages.

Sites live on a host of their own, never the app's: `https://pages.example.com/<owner>/<project>/`
when `CODEHAVEN_PAGES_HOST` is set. Each page runs sandboxed with no cookies, and gets its own
`localStorage` per project. Who can see a site follows the repository: anyone for a public one,
signed-in accounts for an internal one, people with access for a private one. A site admin can
also turn on full mode at `/admin/pages`, which serves sites at `https://<owner>.pages.example.com/`
with no sandbox; it needs a wildcard certificate. The design is `docs/design/pages.md`.

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


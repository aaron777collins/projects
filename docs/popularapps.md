# popularapps

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/popularapps)
- [GitHub Pages Site](http://www.aaroncollins.info/popularapps/)

## 📊 Project Details

- **Primary Language:** JavaScript
- **Languages Used:** JavaScript, CSS, HTML
- **License:** None
- **Created:** September 17, 2026
- **Last Updated:** September 25, 2026

## 📝 About

# Rankwatch

Live App Store chart positions, by country and category — filterable, at a glance.

**[Open the live site →](https://aaron777collins.github.io/popularapps/)**

## What it does

Rankwatch pulls the public iTunes charts feed daily and shows the current
Top Free, Top Paid, and Top Grossing apps across 4 App Store storefronts (US,
UK, Canada, Australia) and 26 categories each, up to 100 apps deep per list
(Apple's feed hard-caps at 100 — no key or workaround gets you further). You can filter by chart type and category,
search by app or developer name, sort by rank/name/price, and see:

- **Overview stats** — apps in view, category count, last updated time, free vs.
  paid split.
- **Movers** — the biggest rank risers and fallers since the previous data
  refresh, once at least two days of history exist.
- **Rank history** — click any app to see its chart position over time.

No backend, no build step. It's a static site that reads two JSON files.

## How it's built

```
scripts/fetch-data.mjs          Fetches the charts, writes data/latest.json and data/history.json
Jenkinsfile                     Runs the fetch daily on Jenkins (dev3), commits the result
.github/workflows/update-data.yml   Manual fallback (workflow_dispatch only) if Jenkins is down
.github/workflows/deploy-pages.yml  Deploys the repo to GitHub Pages on every push to main
index.html, assets/             The dashboard itself — plain HTML/CSS/JS, Chart.js for charts
```

Data source: Apple's public iTunes RSS charts
(`itunes.apple.com/{country}/rss/{chart}/limit=100/genre={id}/json`). No API key
needed. `data/history.json` keeps the last 30 daily snapshots per country/chart/
category, top 100 apps per snapshot — that's what powers the movers panel and
rank-history charts.

## Jenkins setup (one-time, on dev3)

The daily fetch runs on Jenkins instead of GitHub Actions, because dev3 is
Aaron's own box and it's free to run there. To wire it up:

1. **Credential.** Reuses the existing shared `github-credentials`
   credential in Jenkins (username/password from `GITHUB_USERNAME` /
   `GITHUB_TOKEN` in `.env` on dev3) rather than a repo-specific one — the
   Jenkinsfile references it by that ID. If that credential ever needs a
   fresh PAT, github.com → Settings → Developer settings → Fine-grained
   tokens → generate one scoped to `popularapps`, Contents: Read and write,
   and update `GITHUB_TOKEN` in `.env`.
2. **Create the job.** New Item → Pipeline (or Multibranch Pipeline) →
   - Pipeline script from SCM
   - SCM: Git, repo URL `https://github.com/aaron777collins/popularapps.git`
   - Script path: `Jenkinsfile`
3. **Node.** The Jenkinsfile pins `agent { label 'built-in' }` — it runs
   on the Jenkins controller itself, not on `agent-1`, because the
   controller's custom image has Node 20 baked in and `agent-1` (a bare
   `jenkins/inbound-agent` image) doesn't. Confirmed by hitting `node: not
   found` on `agent-1` on the first real run and pinning it after.
4. Trigger a build manually once to confirm it pushes correctly, then let the
   `cron('H 6 * * *')` schedule in the Jenkinsfile take over.

## Running it locally

```bash
python3 -m http.server 8000
```

then open `http://localhost:8000`. (Opening `index.html` directly via `file://`
won't work — the browser blocks `fetch()` of local JSON files under that
protocol.)

To refresh the data yourself:

```bash
node scripts/fetch-data.mjs
```

## Extending it

- **More countries**: add entries to the `COUNTRIES` array in
  `scripts/fetch-data.mjs` (ISO country code Apple's storefronts use, e.g.
  `de`, `fr`, `jp`). The frontend already reads the country list from the data
  file, so no UI changes are needed — but each additional country adds ~78
  requests to the run (~2-3 min at current throughput), so bump the
  `Jenkinsfile`'s `timeout(...)` if you add several at once.
- **More categories**: Apple's genre IDs are listed at the top of
  `scripts/fetch-data.mjs`.


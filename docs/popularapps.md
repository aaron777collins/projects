# popularapps

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/popularapps)
- [GitHub Pages Site](http://www.aaroncollins.info/popularapps/)

## 📊 Project Details

- **Primary Language:** JavaScript
- **Languages Used:** JavaScript, CSS, HTML
- **License:** None
- **Created:** September 17, 2026
- **Last Updated:** September 17, 2026

## 📝 About

# Rankwatch

Live App Store chart positions, by country and category — filterable, at a glance.

**[Open the live site →](https://aaron777collins.github.io/popularapps/)**

## What it does

Rankwatch pulls the public iTunes charts feed every 6 hours and shows the current
Top Free, Top Paid, and Top Grossing apps for the US App Store, broken out across
26 categories. You can filter by chart type and category, search by app or
developer name, sort by rank/name/price, and see:

- **Overview stats** — apps in view, category count, last updated time, free vs.
  paid split.
- **Movers** — the biggest rank risers and fallers since the previous data
  refresh, once at least two days of history exist.
- **Rank history** — click any app to see its chart position over time.

No backend, no build step. It's a static site that reads two JSON files.

## How it's built

```
scripts/fetch-data.mjs          Fetches the charts, writes data/latest.json and data/history.json
.github/workflows/update-data.yml   Runs the fetch every 6 hours, commits the result
.github/workflows/deploy-pages.yml  Deploys the repo to GitHub Pages on every push to main
index.html, assets/             The dashboard itself — plain HTML/CSS/JS, Chart.js for charts
```

Data source: Apple's public iTunes RSS charts
(`itunes.apple.com/{country}/rss/{chart}/limit=100/genre={id}/json`). No API key
needed. `data/history.json` keeps the last 30 daily snapshots per country/chart/
category, which is what powers the movers panel and rank-history charts.

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
  `scripts/fetch-data.mjs`. The frontend already reads the country list from the
  data file, so no UI changes are needed.
- **More categories**: Apple's genre IDs are listed at the top of
  `scripts/fetch-data.mjs`.


# bible-study-lab

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/bible-study-lab)
- [GitHub Pages Site](https://www.aaroncollins.info/bible-study-lab/)

## 📊 Project Details

- **Primary Language:** TypeScript
- **Languages Used:** TypeScript, CSS, HTML
- **License:** Other
- **Created:** November 21, 2026
- **Last Updated:** November 21, 2026

## 📝 About

# Bible Study Lab

A free, private Bible study app for people who want to learn, share and grow. It runs entirely in your browser and is served as static files from GitHub Pages.

**Live:** https://www.aaroncollins.info/bible-study-lab/

## What you can do

- **Read** the KJV, WEB, ASV and Young's Literal Translation. Compare two or three side by side. Words of Jesus in red. Footnotes. Read aloud.
- **See how Scripture connects.** About 345,000 cross references from OpenBible.info, ranked by reader votes: every verse's connections with strength, a network around any verse, a whole-Bible arc view, arcs inside a book, the shortest path between any two verses, the most connected verses and books, and a chapter heat map.
- **Search** words, exact phrases and references such as `Jn 3:16`, in any translation.
- **Study the original words.** Tap a KJV word to see the Hebrew or Greek behind it, how the KJV renders it, and every verse where it appears.
- **Keep notes** with tags, colored highlights, bookmarks, prayers (mark answered later) and guided Observe, Interpret, Apply notes. They live in your browser's IndexedDB, with a clear warning that they can be lost, an export and import of one JSON file, and a reminder until you export.
- **Share** a verse as text, a link, a picture card, or a printable study sheet, and send a whole week of readings as one link (no server involved).
- **Grow:** topics (6,700 of them), reading plans with progress (including M'Cheyne's calendar), a verse of the day, memory verses with spaced review, plain tradition-neutral overviews of all 66 books.
- **Works offline** as an installable app. Choose what to download for a flight.

No accounts, no tracking, no cookies, no paid services. Data sources and licenses are in [DATA.md](DATA.md) and on the About page.

## Develop

Node 26 or newer.

```sh
npm ci
npm run dev            # http://localhost:5173/bible-study-lab/
npm test               # unit tests (Vitest)
npm run build          # type check and production build into dist/
npm run test:e2e       # Playwright (builds are served with vite preview)
npm run data:verify    # checks the committed data in public/data/v1
npm run data           # re-download sources and rebuild the data (needs network)
```

Everything is pinned to exact versions. The design system is shadcn/ui (new-york style, Tailwind v4) with tokens in `src/styles/globals.css`. The plan and the decisions behind it are in [PLAN.md](PLAN.md).

## Layout

```
src/                 the app (React, TypeScript, hash routes)
scripts/             the data pipeline: fetch, build, verify
public/data/v1/      generated data, committed
tests/unit, e2e      Vitest and Playwright
```

## License

App code: MIT. Strong's lexicon files: CC BY-SA 3.0. Cross references and topics: CC BY 4.0 (OpenBible.info). Bible texts: public domain. See [DATA.md](DATA.md).


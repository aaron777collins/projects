# mcsmanager-market

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/mcsmanager-market)
- [GitHub Pages Site](http://www.aaroncollins.info/mcsmanager-market/)

## 📊 Project Details

- **Primary Language:** Python
- **Languages Used:** Python
- **License:** MIT License
- **Created:** October 01, 2026
- **Last Updated:** October 01, 2026

## 🏷️ Topics

`mcsmanager`, `minecraft`

## 📝 About

# mcsmanager-market

An always-fresh app marketplace ("quick install" templates) for the
[MCSManager](https://github.com/MCSManager/MCSManager) panel.

The official market at `https://script.mcsmanager.com/market.json` can lag behind new Minecraft
releases. This repo takes that official market as its base and regenerates the Minecraft server
entries straight from each project's own API, every 6 hours. Everything else in the official
market (Hytale, Terraria, Palworld, Rust, ...) is passed through unchanged.

## Install (30 seconds)

In the MCSManager panel (v10.8.0 or newer), as an administrator:

1. Open **Settings** (panel settings).
2. Find **App Marketplace Data Source** (setting `presetPackAddr`).
3. Set it to:

   ```
   https://raw.githubusercontent.com/aaron777collins/mcsmanager-market/main/market.json
   ```

4. Save, then open the **Marketplace / Quick install** page.

To go back to the official list, set it to `https://script.mcsmanager.com/market.json`.

Alternative URL (GitHub Pages, same content):
`https://aaron777collins.github.io/mcsmanager-market/market.json`

Note: the panel caches the market list in `data/market_cache.json` for up to 12 hours and the
cache does not notice an address change. After switching the address, delete that file (or wait),
otherwise you keep seeing the old list.

Self-hosting the panel with Docker? The file is at `/opt/mcsmanager/web/data/market_cache.json`
inside the container (a bind mount of your `web/data` directory).

## What is generated

| Loader | Source | Notes |
| --- | --- | --- |
| Vanilla | Mojang `piston-meta` | official `server.jar` |
| Fabric | `meta.fabricmc.net` | latest stable installer, installs the server on first run |
| Paper | PaperMC `fill` v3 API | newest STABLE/BETA build per version |
| Folia | PaperMC `fill` v3 API | newest STABLE/BETA build per version |
| Purpur | `api.purpurmc.org` | latest build per version (see note below) |
| Forge | Forge promotions + maven | latest build, Linux and Windows entries |
| NeoForge | NeoForged maven metadata | newest stable build, else newest beta; Linux and Windows entries |

Versions: the newest four Mojang release lines of the new scheme (currently 26.3, 26.2, 26.1.2),
plus 1.21.11, 1.21.10, 1.21.8, 1.21.4 and 1.21.1 (and Forge 1.20.1). A loader only gets a version
if it actually publishes a build for it.

The required Java version of every entry comes from Mojang's per-version `javaVersion` field and
the Docker image is the matching `eclipse-temurin:<n>-jdk`. Entry titles, descriptions, commands and
field layout are copied from the official entries, so the panel treats them like official ones.

Purpur note: the official download URL has no file name, so the entry downloads to a file called
`download` (the start command is `java ... -jar download nogui`). It is a normal Purpur jar.

## How it updates

`generate.py` (Python 3, standard library only) does the following:

1. Download the official market.
2. Regenerate the entries above and replace the official entries of those loaders.
3. Validate: valid JSON, same keys as official entries, no duplicate title/description, and every
   generated download URL answers with a success status.
4. Write `market.json` only if the content changed.

A Jenkins pipeline (`Jenkinsfile`) runs this every 6 hours and commits only when `market.json`
changed, so the git history is a changelog. If any validation step fails nothing is published
and the previous file stays online. If one loader's API is down, the previous entries of that
loader are kept.

Run it yourself:

```
python3 generate.py            # generate, validate and write market.json
python3 generate.py --check    # only validate the existing market.json
python3 generate.py --strict   # fail if any loader cannot be generated
```

Tweak the version policy at the top of `generate.py` (`NEW_SCHEME_LINES`, `LEGACY_VERSIONS`,
`EXTRA_VERSIONS`).

## Credits

All non-Minecraft entries, the entry format and the base list come from the official
[MCSManager](https://github.com/MCSManager/MCSManager) project and its market. This repo is
unofficial and not affiliated with MCSManager, Mojang, Fabric, PaperMC, Purpur, Forge or NeoForged.

## License

MIT, see `LICENSE`. Applies to the generator and repo contents; entries originating from the
upstream market remain the property of their authors.


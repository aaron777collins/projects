# caffeinate-menu

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/caffeinate-menu)

## 📊 Project Details

- **Primary Language:** Swift
- **Languages Used:** Swift, Shell
- **License:** MIT License
- **Created:** September 17, 2026
- **Last Updated:** September 17, 2026

## 📝 About

# Caffeinate

A menu bar app that keeps your Mac awake. It is a friendly wrapper around the `caffeinate` command that ships with macOS, so it installs no new binaries. The app runs that same built-in tool and gives it a menu, presets and a visible end time.

## Presets

Three presets cover the common cases:

- **For Claude and visual work (Recommended).** Screen stays on so screenshots and the Simulator window work. Everything else is kept awake too.
- **For background jobs.** Builds, tests and servers keep running. The screen can sleep.
- **Screen only.** Stops the screen dimming. The Mac can still sleep when idle.

## Keep awake settings

- **Screen.** Screen stays on. Turn off to let it sleep and lock.
- **Mac when idle.** Stops sleep when you step away. Recommended.
- **Mac on power.** Stops sleep while plugged in. Recommended.
- **Disk.** Keeps the disk from idling.
- **Mark as in use.** Tells macOS someone is here. Resets idle timers.

If you turn every one of these off, Caffeinate turns itself off.

## How long

Caffeinate can run for 1 hour, 4 hours, 12 hours (overnight), 1 week (recommended) or until you turn it off. The time always counts from the moment you start it or change it, and the menu shows when it will end.

## Lid

**Stay awake with lid closed** makes closing the lid turn off the screen only, so the Mac keeps running. It changes a power setting with the `pmset` tool that ships with macOS and asks for your administrator password. Turn it off before bagging your Mac.

## Install

Clone the repository and cd into the folder, then run:

```sh
./build.sh install
```

That builds the app, copies it to ~/Applications and opens it. Plain `./build.sh` just builds into `build/`.

Requires macOS 14.4 or newer on Apple silicon.

## License

MIT, see [LICENSE](LICENSE).


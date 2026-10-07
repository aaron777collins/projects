# msixrun

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/msixrun)

## 📊 Project Details

- **Primary Language:** PowerShell
- **Languages Used:** PowerShell, Shell
- **License:** MIT License
- **Created:** October 01, 2026
- **Last Updated:** October 06, 2026

## 📝 About

# msixrun

Install and launch an `.msix` / `.msixbundle` / `.appx` package on Windows with one command.
Give it a file or a web address. It installs the package and starts the app.

If Windows does not trust whoever signed the package, msixrun shows you the signer, asks once,
and (after you say yes and approve one Windows permission prompt) trusts that one publisher on
this PC and finishes the install.

## PowerShell (nothing to install)

Paste this into PowerShell, with the package's address or path at the end:

```powershell
& ([scriptblock]::Create((irm https://raw.githubusercontent.com/aaron777collins/msixrun/main/msixrun.ps1))) https://example.com/App.msix
```

- Works in Windows PowerShell 5.1 (the one built into Windows) and PowerShell 7.
- The script itself is not saved to disk and your execution policy is not changed. A package address is downloaded to a temporary folder, and a package path containing `[ ] * ?` or a backtick is copied there; both are deleted when msixrun finishes.
- You do not need Git Bash.

Add switches after the address:

```powershell
& ([scriptblock]::Create((irm https://raw.githubusercontent.com/aaron777collins/msixrun/main/msixrun.ps1))) C:\Downloads\App.msix -NoLaunch -Trust
```

You can also save `msixrun.ps1` and run it: `.\msixrun.ps1 App.msix`.

## Git Bash, MSYS2 or WSL

Install once:

```bash
curl -fsSL https://raw.githubusercontent.com/aaron777collins/msixrun/main/install.sh | bash
```

This puts `msixrun` in `~/.local/bin` (or `$PREFIX/bin`). Add that directory to your `PATH` if needed. Then:

```bash
msixrun https://example.com/App.msix           # download, install, launch
msixrun path/to/app.msix                       # install and launch
msixrun path/to/app.msixbundle --no-launch     # install only
msixrun path/to/app.msix --trust               # trust the publisher without asking
msixrun --help
```

## Switches

| PowerShell | Bash | What it does |
| --- | --- | --- |
| `-NoLaunch` | `--no-launch` | Install only. Do not start the app. |
| `-Trust` | `--trust` | If Windows does not trust the publisher, trust that publisher without asking. |
| `-Yes` | `--yes`, `-y` | Answer yes to every question (see below). |

`-Trust` only covers trusting the publisher. Removing an older app or installing an unsigned
package needs `-Yes`, because those are bigger decisions.

## When Windows does not trust the publisher

Most test and side-loaded packages are signed with a certificate Windows does not know. The
install fails with an error such as `0x800B0109`. msixrun then:

1. Reads the signer of this package. If the signature is broken (for example `HashMismatch`) or
   missing, msixrun refuses and offers nothing for trust. It goes on only when the signature is
   valid but its chain is not trusted (status `UnknownError` or `NotTrusted`).
2. Shows the signer's name, SHA-1 thumbprint and expiry date, and asks:
   `Windows does not trust the publisher of this package. Trust <name> and install? [y/N]`
   Compare the thumbprint with the one the publisher gave you. Control and invisible Unicode
   characters in the name are shown as `?`, and very long names are cut.
3. On yes, reads the signer again and goes on only if its thumbprint is exactly the one you were
   shown and its signature status is still `UnknownError` or `NotTrusted`. Otherwise it stops and
   changes nothing. It then saves that one certificate to a temporary `.cer` file and starts an
   elevated step that is given only the file's path and the expected thumbprint, not the
   certificate itself. The elevated step loads the file, works out the thumbprint again, refuses
   unless it matches the one you were shown, and only then imports it into the **Local Machine,
   Trusted People** store. This needs administrator rights, so Windows shows one permission (UAC)
   prompt. The temporary file is deleted afterwards.
4. Checks the certificate is now in Trusted People and tries the install again.

What this does and does not do:

- It trusts the signer of **this package only**, on **this PC only**.
- It uses **Trusted People**, never the Root store. Windows will install packages signed by that
  certificate, but the certificate is not made a trusted authority for anything else.
- It only happens after you say yes (or pass `-Trust` / `--trust` / `-Yes` / `--yes`). With no
  terminal to ask and no switch, msixrun stops and tells you which switch to use.
- If you decline the permission prompt, nothing is changed.
- To undo it later, open `certlm.msc`, go to Trusted People > Certificates, and delete the entry.

## Other things msixrun handles

- **Unsigned package** (`0x800B0100`). If Developer Mode is on and your Windows supports it,
  msixrun offers to install it unsigned (`Add-AppxPackage -AllowUnsigned`). If Developer Mode is
  off it says how to turn it on: Windows 11 under Settings > System > For developers, Windows 10
  under Settings > Update & Security > For developers.
- **An older copy from a different publisher.** Windows will not update an app across
  publishers. msixrun asks: `An older <name> from a different publisher is installed. Remove it
  and install this one? Its local data will be removed. [y/N]` and, on yes, removes it and installs.
  It asks only when Windows reports the publisher conflict (`0x80073CFB`, or `0x80073CF3` when the
  message also says the package conflicts with or comes from a different publisher) and a copy
  from a different publisher is installed. `0x80073CF3` alone is Windows' generic "dependency or
  conflict validation" failure (a missing framework returns it too), so it never leads to a removal. Any other install error is shown as it is, and
  nothing is removed, even with `-Yes`.
- **Downloads.** For a URL, msixrun downloads the file to a temporary folder and deletes it
  afterwards (TLS 1.2 is forced on Windows PowerShell 5.1).
- **Paths with `[ ] * ?` or a backtick.** Windows treats the first four as wildcards and the backtick as their escape character, so msixrun installs from a plain
  copy in a temporary folder and deletes it afterwards.

## How it works

1. Gets the package (local path, or download from the URL).
2. Reads the package name from the manifest inside the package (it is a zip).
3. Runs `Add-AppxPackage`. If that fails, it recognizes the failure, fixes that one thing (trust
   the publisher, install unsigned, or remove an older copy from another publisher, each once and
   each with your consent) and retries. A failure it does not recognize is shown and stops.
   It recognizes a failure by the HRESULT in Windows' message, after removing the package's path
   and file name from the text (a package called `0x80073CFB.msix` is not an error code). It looks
   at the wording only when the message has no HRESULT.
4. Looks up the installed `PackageFamilyName` and the first app `Id`, and launches with
   `explorer.exe "shell:AppsFolder\<PFN>!<AppId>"`.

The Bash version does the same through `powershell.exe`, converting paths with `cygpath -w` or
`wslpath -w`. No text read from a package is pasted into a command, with one narrow exception:
the signer's thumbprint is passed to the elevated command, and only after it has been checked to
be exactly 40 uppercase hex characters. Apart from that, the only value placed in a PowerShell
script is the package path, quoted, plus the path of the temporary `.cer` file. The elevated step
is passed to PowerShell as a Base64 `-EncodedCommand`, started by its full path under `%SystemRoot%` so a file
named `powershell.exe` in the current folder is never run.

The one-liner is meant for an interactive prompt. If you paste it inside a saved `.ps1` file it
still does not end that script; it sets `$LASTEXITCODE` and returns.

## Tests

```bash
bash test/run.sh                          # Bash version, with stubbed powershell.exe, curl and friends
pwsh -File tests/Invoke-Tests.ps1         # PowerShell version and the Bash version's PowerShell snippets (parsed, and run with the Windows commands replaced), Pester 5
pwsh -File tests/Invoke-Lint.ps1          # PSScriptAnalyzer, incl. Windows PowerShell 5.1 syntax
shellcheck msixrun install.sh test/run.sh
```

The Pester tests mock every Windows command, so they also run on macOS and Linux. That means they
do not prove the real Windows behavior (exception shapes, UAC, `Add-AppxPackage` under Windows
PowerShell 5.1 and PowerShell 7). Run it once on a real Windows machine before a release.

## License

MIT


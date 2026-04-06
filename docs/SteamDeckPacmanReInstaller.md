# SteamDeckPacmanReInstaller

⭐ 1 stars

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/SteamDeckPacmanReInstaller)

## 📊 Project Details

- **Primary Language:** Shell
- **Languages Used:** Shell
- **License:** None
- **Created:** December 31, 2023
- **Last Updated:** February 19, 2026

## 📝 About

# SteamDeckInstallerManager
My code for managing pacman installations to allow easy re-installing after a steam update.

## Install
First, make sure you have root access by creating a password using the following command:
```bash
passwd
```

Then, if you haven't already, run the following command to disable read-only mode for Steam-OS to make pacman installs work:
```bash
sudo steamos-readonly disable
```

Finally, the following command does the following:
1. Clones the repo to Programs/install_everything
2. Makes install_everything a runnable command
3. Backs up the bashrc
4. Edits the bashrc adds all folders within the Programs folder to be on PATH so you can make other scripts easily too. This also makes the current script, install_everything, runnable from anywhere. You'll still want to edit the programs.txt file to add the programs you want to install though.
```bash
mkdir -p /home/deck/Programs/install_everything && \
git clone https://github.com/aaron777collins/SteamDeckPacmanReInstaller.git /home/deck/Programs/install_everything && \
sudo chmod +x /home/deck/Programs/install_everything/install_everything && \
cp ~/.bashrc ~/.bashrc.backup.$(date +%Y%m%d%H%M%S) && \
if grep -q '# If not running interactively, don'\''t do anything' ~/.bashrc; then \
    sed -i '/# If not running interactively, don'\''t do anything/i # Adding all folders within Programs to PATH\nfor dir in /home/deck/Programs/*; do\n    if [[ -d "$dir" && ":$PATH:" != *":$dir:"* ]]; then\n        PATH="$dir:$PATH"\n    fi\ndone\n' ~/.bashrc; \
else \
    echo -e "# Adding all folders within Programs to PATH\nfor dir in /home/deck/Programs/*; do\n    if [[ -d \"\$dir\" && \":\$PATH:\" != *\":\$dir:\"* ]]; then\n        PATH=\"\$dir:\$PATH\"\n    fi\ndone" >> ~/.bashrc; \
fi
```


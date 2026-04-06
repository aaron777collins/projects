# tmux-config

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/tmux-config)

## 📊 Project Details

- **Primary Language:** Shell
- **Languages Used:** Shell
- **License:** None
- **Created:** May 17, 2023
- **Last Updated:** June 10, 2023

## 📝 About

# tmux-config
This is my basic tmux config. I'm still learning tmux so this will change as I improve. 
- It goes well with my [vim-config](https://github.com/aaron777collins/vim-config). 

- Make sure to install [tpm](https://github.com/tmux-plugins/tpm) to allow for tmux plugins. You'll need to run `[your prefix] + I` to install the plugins after installing tpm.
Note: You may want to run
```bash
chmod u+x starttmux
```
and copy it `to /usr/local/bin` to run vim inside a tmux session at a specified location. For example
```bash
starttmux somefolder
```
would open a tmux and vim session in [your current directory]/somefolder. You can use relative or absolute pathing because it just runs the `cd` command to navigate.


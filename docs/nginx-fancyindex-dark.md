# nginx-fancyindex-dark

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/nginx-fancyindex-dark)

## 📊 Project Details

- **Primary Language:** HTML
- **Languages Used:** HTML
- **License:** MIT License
- **Created:** February 05, 2026
- **Last Updated:** February 05, 2026

## 📝 About

# nginx-fancyindex-dark

A dark GitHub-style theme for [nginx-fancyindex](https://github.com/aperezdc/ngx-fancyindex) with built-in file preview modal.

![Preview](https://img.shields.io/badge/style-dark-1a1b26?style=flat-square) ![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

## Features

- 🌙 **Dark theme** — GitHub-inspired dark mode colors
- 📄 **File preview** — Click text files to preview in a modal (no page reload)
- ⌨️ **Keyboard friendly** — Press Escape to close previews
- 📱 **Responsive** — Works on mobile and desktop
- 🚀 **Zero dependencies** — Pure HTML/CSS/JS

## Supported Preview Extensions

`.log`, `.txt`, `.csv`, `.json`, `.md`, `.xml`, `.yaml`, `.yml`, `.conf`, `.ini`, `.sh`, `.py`, `.js`, `.html`, `.css`

## Installation

1. Install nginx with fancyindex module:
```bash
sudo apt install nginx libnginx-mod-http-fancyindex
```

2. Copy theme files:
```bash
sudo mkdir -p /var/www/static/fancyindex-theme
sudo cp header.html footer.html /var/www/static/fancyindex-theme/
```

3. Configure nginx:
```nginx
server {
    listen 80;
    server_name _;
    
    root /var/www/static;
    
    fancyindex on;
    fancyindex_exact_size off;
    fancyindex_localtime on;
    fancyindex_header "/fancyindex-theme/header.html";
    fancyindex_footer "/fancyindex-theme/footer.html";
    fancyindex_time_format "%b %d, %Y %H:%M";
    
    location / {
        try_files $uri $uri/ =404;
    }
}
```

4. Reload nginx:
```bash
sudo nginx -t && sudo systemctl reload nginx
```

## How It Works

- Clicking a previewable file fetches the first 512KB via a Range request
- Shows up to 200 lines in a modal overlay
- Click outside, press Escape, or click Close to dismiss
- Download button gets the full file

## Customization

Edit `header.html` to change colors. Key CSS variables:
- `#0d1117` — Background
- `#161b22` — Secondary background
- `#c9d1d9` — Text color
- `#58a6ff` — Links/accents
- `#30363d` — Borders

## License

MIT


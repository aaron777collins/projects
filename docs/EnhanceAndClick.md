# EnhanceAndClick

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/EnhanceAndClick)

## 📊 Project Details

- **Primary Language:** Python
- **Languages Used:** Python
- **License:** None
- **Created:** January 27, 2026
- **Last Updated:** January 28, 2026

## 📝 About

# EnhanceAndClick

An AI-friendly iterative zoom-and-click tool for precise UI automation. Instead of guessing pixel coordinates from a full screenshot, progressively zoom into quadrants until your target is big and centered, then save it as a reusable template.

## Why?

When AI agents need to click UI elements, they typically:
1. Take a screenshot
2. Try to guess pixel coordinates from the full image
3. Miss by 50 pixels and click the wrong thing

**EnhanceAndClick** solves this by letting the AI iteratively "enhance" (zoom) into the target area until it's confident, then save that view as a template for future clicks.

## Installation

```bash
# Dependencies
pip install pyautogui opencv-python numpy
sudo apt install scrot imagemagick  # Linux

# Install
git clone https://github.com/aaron777collins/EnhanceAndClick.git
cd EnhanceAndClick
chmod +x zoomclick.py
sudo ln -s $(pwd)/zoomclick.py /usr/local/bin/zoomclick
```

## Workflow

### 1. Start a session
```bash
zoomclick --start
```
Returns a screenshot with quadrant overlay:
- **Red lines** divide into 4 quadrants
- **Green box** shows the center region

### 2. Zoom iteratively
```bash
zoomclick --zoom top-left      # or: top-right, bottom-left, bottom-right, center
zoomclick --zoom center        # keep zooming until target is BIG and CENTERED
```
Each zoom returns a new cropped image. Keep zooming until your target element fills most of the image.

### 3. Save as template
```bash
zoomclick --save "submit_button"
```
Saves the current zoomed region for future clicking:
- Cropped image (for template matching)
- Center coordinates (fallback)

### 4. Click anytime
```bash
zoomclick --click "submit_button"
```
Finds the template on screen using OpenCV and clicks its center.

## Commands

| Command | Description |
|---------|-------------|
| `--start` | Start new session with full screenshot + overlay |
| `--zoom <quadrant>` | Zoom into quadrant |
| `--save <name>` | Save current view as named template |
| `--click <name>` | Find and click saved template |
| `--click-center` | Click center of current viewport |
| `--list` | List all saved templates |
| `--reset` | Reset zoom session |
| `--delete <name>` | Delete a saved template |
| `--no-click` | With --click, locate but don't click |

## Example Session

```bash
# Want to click a "Submit" button on a webpage

zoomclick --start
# → Analyze screenshot, target is in bottom-right

zoomclick --zoom bottom-right
# → Getting closer, target now in top-left of this view

zoomclick --zoom top-left
# → Target is big and centered!

zoomclick --save "submit_btn"
# → Template saved at ~/.zoomclick/templates/submit_btn.png

# Later, click it anytime:
zoomclick --click "submit_btn"
# → Finds button on screen, clicks it
```

## Storage

- **Templates:** `~/.zoomclick/templates/` (persistent)
- **Working files:** `/tmp/zoomclick/` (temporary)
- **State:** `/tmp/zoomclick/state.json` (current session)

## How It Works

1. Each zoom halves the viewport dimensions
2. 3-4 zooms: 1920×1080 → 960×540 → 480×270 → 240×135
3. Template matching uses OpenCV with adaptive confidence (starts at 100%, decreases until found)
4. Falls back to saved coordinates if matching fails

## For AI Agents

The tool outputs JSON for easy parsing:

```json
{
  "success": true,
  "action": "zoom",
  "quadrant": "center",
  "screenshot": "/tmp/zoomclick/overlay_1_1234567890.png",
  "viewport": {
    "x": 480, "y": 270,
    "width": 960, "height": 540,
    "zoom_level": 1
  },
  "screen_coords": {
    "center_x": 960,
    "center_y": 540
  }
}
```

## License

MIT


# bible-drawing-pipeline

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/bible-drawing-pipeline)

## 📊 Project Details

- **Primary Language:** Shell
- **Languages Used:** Shell
- **License:** None
- **Created:** February 07, 2026
- **Last Updated:** February 07, 2026

## 📝 About

# Bible Drawing Video Pipeline

Automated video editing pipeline for Aaron's Bible drawing project.

## Quick Start

```bash
# Process a single video
bdp process /path/to/recording.mp4

# Or use the folder watcher
bdp watch --daemon
# Then drop videos into: ~/bible-drawing-pipeline/input/
# Edited videos appear in: ~/bible-drawing-pipeline/output/
```

## What It Does

1. **Silence Removal** - Cuts dead air and long pauses automatically
2. **Transcription** - Converts your reading to text using Whisper AI
3. **Filler Word Detection** - Identifies "um", "uh", etc. for removal
4. **Subtitle Generation** - Creates .srt file for YouTube upload
5. **Audio Normalization** - Consistent volume levels (-14 LUFS broadcast standard)
6. **Thumbnail Extraction** - Grabs a nice frame from your drawing
7. **High Quality Export** - YouTube-optimized MP4

## Commands

```bash
bdp process <video>      # Process a single video
bdp watch                # Start folder watcher (foreground)
bdp watch --daemon       # Start folder watcher (background)
bdp watch --stop         # Stop folder watcher
bdp watch --status       # Check if watcher is running
bdp status               # Show pipeline status
```

## Output Files

For each video processed, you get:
- `*_edited.mp4` - The final edited video
- `*_subtitles.srt` - Subtitle file for YouTube
- `*_transcript.txt` - Full text transcript
- `*_thumbnail.jpg` - Auto-generated thumbnail

## Options

```bash
# Adjust silence detection (default: 0.5s at -35dB)
bdp process video.mp4 --silence-threshold 0.3 --silence-level -30

# Use larger Whisper model for better accuracy
bdp process video.mp4 --whisper-model medium

# Skip subtitle generation
bdp process video.mp4 --no-subtitles

# Enable Slack notification when done
bdp process video.mp4 --notify
```

## Folder Structure

```
~/bible-drawing-pipeline/
├── input/           # Drop raw videos here
├── output/          # Edited videos appear here
├── processing/      # Temporary work files
├── scripts/         # Pipeline scripts
├── config.sh        # Customizable settings
└── bdp              # Main CLI
```

## Tips

- **Silence threshold**: Start with 0.5s. If too much is cut, try 0.7s. If not enough, try 0.3s.
- **Whisper model**: `base` is fast and good. Use `medium` or `large` for better accuracy on quiet/unclear audio.
- **OBS setup**: Record in 1080p, 30fps, high bitrate for best results.

## Sophie Integration

Sophie can:
- Process videos on request ("Sophie, edit my latest recording")
- Monitor the pipeline ("Sophie, check video pipeline status")
- Get notified when processing completes and ping you in Slack


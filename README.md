# FileToLink Bot

A Telegram bot that converts files to streamable links with a Netflix-style web interface for watching videos and downloading files.

## Features

- 🎬 **Video Streaming**: Watch videos directly in browser with a Netflix-style player
- 🎵 **Audio Streaming**: Listen to audio files with built-in player
- 📁 **File Downloads**: Download any file type with a modern download page
- 📱 **Mobile Responsive**: Works perfectly on all devices
- 🎯 **External Player Support**: Open videos in MX Player, VLC, and other external players
- 🔗 **Direct Links**: Generate direct download/stream links for any file

## Demo

- **Video Streaming**: Modern video player with playback controls
- **Download Page**: Clean, Netflix-style download interface
- **Mobile Friendly**: Optimized for mobile devices

## Setup

### Prerequisites

- Python 3.8 or higher
- Telegram Bot Token
- Telegram API ID and Hash

### Installation

1. Clone the repository:
```bash
git clone https://github.com/MeeRazi/FileToLink.git
cd FileToLink
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure the bot:
   - Copy `config_sample.env` to `config.env`
   - Edit `config.env` with your credentials:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
BIN_CHANNEL=-100xxxxxxxxx
STREAM_URL=https://your-domain.com/
```

4. Run the bot:
```bash
python bot.py
```

## Configuration

### Required Variables

- `API_ID`: Get from [my.telegram.org](https://my.telegram.org)
- `API_HASH`: Get from [my.telegram.org](https://my.telegram.org)
- `BOT_TOKEN`: Get from [@BotFather](https://t.me/botfather)
- `BIN_CHANNEL`: Channel ID where files will be stored
- `STREAM_URL`: Your domain URL for streaming

## Usage

1. **Send any file** to the bot
2. **Get a link** to stream/download the file
3. **Share the link** with anyone

### Supported Formats

- **Video**: MP4, AVI, MKV, OGG, and more
- **Audio**: MP3, MP4, WAV, and more
- **Files**: Any file type for download

## Web Interface

### Video/Audio Streaming (`/watch/{message_id}`)
- Netflix-style dark theme
- Video.js player with advanced controls
- Mobile-responsive design
- External player integration
- Download functionality

### File Download (`/download/{message_id}`)
- Clean download interface
- File information display
- Progress indicators
- Mobile-optimized

## Deployment

### Docker

```bash
docker build -t filetolink-bot .
docker run -d --name filetolink -p 8080:8080 filetolink-bot
```

## Support

- **Telegram**: [@BotSync](https://t.me/botsync)
- **Issues**: [GitHub Issues](https://github.com/MeeRazi/FileToLink/issues)
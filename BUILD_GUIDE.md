# SowardBot Build Configuration

This document contains the build instructions for creating the SowardBot.exe executable with the premium dashboard.

## Prerequisites

- **Python 3.8+** - Download from [python.org](https://www.python.org)
- **Node.js 16+** - Download from [nodejs.org](https://nodejs.org)
- **Windows, macOS, or Linux** - The build process works on all platforms

## Build Instructions

### Step 1: Install Dependencies

```bash
pip install -r build_requirements.txt
```

### Step 2: Build the .EXE (Windows)

Run the build script:
```bash
build.bat
```

Or use PyInstaller directly:
```bash
pyinstaller pyinstaller.spec
```

The built .EXE will be located in `dist/SowardBot.exe`

### Step 3: Build on macOS/Linux

Run the build script:
```bash
chmod +x build.sh
./build.sh
```

The executable will be in `dist/SowardBot`

## Running the Bot

### Using the .EXE

Simply double-click `dist/SowardBot.exe` (Windows) or run `dist/SowardBot` (macOS/Linux)

### Using Python Directly

```bash
pip install -r requirements.txt
python launcher.py
```

## Dashboard Access

Once the bot is running:

1. The dashboard will be available at `http://localhost:8000`
2. Use your bot token to login
3. Manage all bot features from the premium dashboard

## Features

### Core Features
- ✅ Discord Bot (runs with Lavalink for music)
- ✅ FastAPI Server (port 8000)
- ✅ React Premium Dashboard

### Dashboard Features
- 📊 **Dashboard** - Real-time bot statistics
- ⚔️ **Moderation** - Ban/mute management
- 🎵 **Music** - Music player controls
- 💰 **Economy** - Currency and leaderboards
- 📝 **Logs** - Event logging and monitoring
- 👥 **Users** - User management interface
- ⚙️ **Settings** - Bot configuration

## Configuration

Create a `.env` file in the project root:

```env
TOKEN=your_discord_bot_token
DATABASE_URL=postgresql://user:password@localhost/soward
LAVALINK_HOST=localhost
LAVALINK_PORT=2333
LAVALINK_PASSWORD=youshallnotpass
```

## Troubleshooting

### Bot won't start
- Check that your bot token is valid
- Ensure the bot has the required Discord permissions
- Check logs in the console for detailed errors

### Dashboard won't open
- Ensure port 8000 is not in use
- Check firewall settings
- Try accessing `http://127.0.0.1:8000` instead of `localhost:8000`

### Build failures
- Delete `dist/` and `build/` folders and try again
- Ensure all dependencies are installed: `pip install -r build_requirements.txt`
- For React errors, delete `dashboard/node_modules` and run `npm install` in the `dashboard/` folder

## Support

For issues and questions, refer to the project documentation or create an issue on GitHub.

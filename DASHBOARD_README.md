# SowardBot .EXE & Premium Dashboard Setup

## 📋 Quick Start

### Build the .EXE Executable (Windows)

```bash
# 1. Install dependencies
pip install -r build_requirements.txt

# 2. Run the build script
build.bat

# 3. Run the bot
dist/SowardBot.exe
```

### macOS/Linux

```bash
chmod +x build.sh
./build.sh
./dist/SowardBot
```

## 📊 Dashboard Features

The premium dashboard includes:

### 📈 Dashboard
- Real-time bot statistics
- Server and user metrics
- Commands executed counter
- Bot uptime display
- Quick action buttons

### ⚔️ Moderation Panel
- Ban management
- Mute management
- User sanctioning interface
- Moderation logs

### 🎵 Music Player
- Now playing display
- Music queue management
- Skip and pause controls
- Album art display

### 💰 Economy System
- Currency statistics
- Richest users leaderboard
- User levels and balance
- Transaction tracking

### 📝 Event Logs
- Real-time event logging
- Filterable log entries
- Message events
- Moderation events
- Member join/leave events

### 👥 User Management
- User directory
- Search functionality
- Member statistics
- Level and message counts

### ⚙️ Settings
- Bot configuration
- Prefix customization
- Language selection
- Feature toggles
- Premium features overview

## 🔧 Configuration

1. Copy `.env.example` to `.env`
2. Fill in your Discord bot token
3. Configure database and Lavalink settings
4. Run the application

## 📦 What's Included

- **Launcher.py** - Entry point that runs both bot and API
- **PyInstaller.spec** - Configuration for creating the .EXE
- **Dashboard/** - Complete React frontend
- **Build Scripts** - Automated build process

## 🚀 Running

The .EXE starts:
1. Discord bot (connects to Discord)
2. FastAPI server (port 8000)
3. React dashboard (accessible via web browser)

## 📱 Access Dashboard

Once running:
- Open browser to `http://localhost:8000`
- Login with your bot token
- Full premium dashboard access

## 📖 Full Documentation

See [BUILD_GUIDE.md](BUILD_GUIDE.md) for detailed build instructions.

See [API_ENDPOINTS.md](API_ENDPOINTS.md) for API route information.

## ✨ Premium Features

✅ Advanced moderation tools  
✅ Music player integration  
✅ Economy system  
✅ Custom welcome messages  
✅ Analytics & logging  
✅ Auto backup  
✅ Custom roles  
✅ Giveaway manager  
✅ Ticket system  
✅ AFK system  
✅ Full dashboard control  

## 🐛 Troubleshooting

**Bot won't start:**
- Verify bot token in .env
- Check Discord permissions
- View console for error details

**Dashboard won't open:**
- Ensure port 8000 is available
- Check firewall settings
- Try `http://127.0.0.1:8000`

**Build fails:**
- Delete `dist/` and `build/` folders
- Reinstall dependencies: `pip install -r build_requirements.txt`
- For React errors: delete `dashboard/node_modules` and run `npm install`

## 💡 Tips

- The .EXE runs everything in one process (bot + API)
- Dashboard auto-refreshes every 30 seconds
- All settings are saved to database
- Logs are viewable in real-time from dashboard

---

**Created:** Premium Dashboard for SowardBot  
**Status:** Production Ready

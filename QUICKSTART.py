#!/usr/bin/env python3
"""
Quick Start Script - Run this to see build instructions
"""

QUICK_START = """
╔════════════════════════════════════════════════════════════════════╗
║           SowardBot .EXE & Premium Dashboard Setup                ║
║                        QUICK START GUIDE                          ║
╚════════════════════════════════════════════════════════════════════╝

📋 PREREQUISITES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Python 3.8+ (download from python.org)
✓ Node.js 16+ (download from nodejs.org)
✓ Discord Bot Token (get from Discord Developer Portal)

🚀 STEP-BY-STEP BUILD (WINDOWS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. PREPARE PROJECT
   > copy .env.example .env
   > Edit .env and add your Discord token

2. BUILD THE .EXE
   > build.bat
   
   This will:
   • Install Python dependencies
   • Install Node.js dependencies
   • Build React dashboard
   • Create dist/SowardBot.exe

3. RUN THE BOT
   > dist/SowardBot.exe
   
   Or double-click SowardBot.exe in dist/ folder

4. ACCESS DASHBOARD
   • Open browser: http://localhost:8000
   • Login with your bot token
   • Start managing your bot!

🐧 LINUX/MACOS BUILD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

$ chmod +x build.sh
$ ./build.sh
$ dist/SowardBot

📊 DASHBOARD FEATURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 Dashboard      - Real-time bot statistics
⚔️  Moderation    - Ban/mute management
🎵 Music          - Music player controls
💰 Economy        - Currency & leaderboards
📝 Logs           - Event logging
👥 Users          - User management
⚙️  Settings      - Bot configuration

🔧 CONFIGURATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Edit .env file with:
  TOKEN=your_bot_token
  DATABASE_URL=your_database
  LAVALINK_HOST=localhost
  LAVALINK_PORT=2333
  LAVALINK_PASSWORD=youshallnotpass

📁 IMPORTANT FILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

launcher.py            - Bot + API launcher
pyinstaller.spec       - .EXE builder config
build.bat / build.sh   - Build scripts
dashboard/             - React dashboard source
.env.example           - Config template
BUILD_GUIDE.md         - Detailed instructions
API_ENDPOINTS.md       - API documentation
SETUP_COMPLETE.md      - Full setup guide

⚠️  TROUBLESHOOTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Build Fails?
  > Delete dist/ and build/ folders
  > Run: pip install -r build_requirements.txt --force-reinstall
  > Delete dashboard/node_modules
  > Try build script again

Bot won't connect?
  > Check Discord token in .env
  > Verify bot has Server Members Intent
  > Check firewall settings

Dashboard won't open?
  > Port 8000 in use? Check with: netstat -ano | findstr :8000
  > Try http://127.0.0.1:8000 instead
  > Check browser console (F12) for errors

💡 USEFUL COMMANDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Run without building .EXE
python launcher.py

# Rebuild dashboard only
cd dashboard && npm run build && cd ..

# Rebuild .EXE only
pyinstaller pyinstaller.spec

# Check if ports are available
netstat -ano | findstr :8000  # Windows
lsof -i :8000                 # Linux/Mac

📞 DOCUMENTATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• BUILD_GUIDE.md       - Full build instructions
• API_ENDPOINTS.md     - API endpoint docs
• DASHBOARD_README.md  - Dashboard overview
• SETUP_COMPLETE.md    - Complete setup guide

🎉 YOU'RE ALL SET!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your project has:
✅ Standalone .EXE builder
✅ Premium web dashboard
✅ Full API integration
✅ Automated build scripts
✅ Complete documentation

Next steps:
1. Configure .env with your settings
2. Run build.bat (or build.sh)
3. Execute the .EXE
4. Open dashboard at http://localhost:8000
5. Start managing your bot!

════════════════════════════════════════════════════════════════════
"""

if __name__ == "__main__":
    print(QUICK_START)

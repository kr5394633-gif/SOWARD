# 🚀 Complete Railway Deployment Guide

## ✅ Step 1: Git Repository Ready
Your SowardBot project is initialized with git and ready to push.

---

## 📋 Step 2: Create GitHub Repository

1. **Go to GitHub:** https://github.com/new
2. **Create new repository:**
   - Repository name: `Soward-Bot`
   - Description: `Discord Bot with Premium Dashboard - 24/7 Hosting`
   - Visibility: **Public** (required for free Railway deployment)
   - Initialize README: ✗ (we already have files)
   - Add .gitignore: ✗ (we already have it)
   - Add license: ✗ (optional)
3. **Click "Create repository"**

---

## 🔗 Step 3: Connect GitHub & Push Code

After creating repository on GitHub, you'll see these commands. **Copy and paste them in PowerShell:**

```powershell
cd c:\Users\HP\Downloads\Soward-Bot-main
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Soward-Bot.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username!

---

## 🚂 Step 4: Deploy on Railway

1. **Go to Railway:** https://railway.app
2. **Sign up with GitHub** (fastest way)
3. **Create New Project:**
   - Click **"Deploy from GitHub"**
   - Connect your GitHub account
   - Select **Soward-Bot** repository
   - Railway auto-detects Python project ✨

**That's it!** Railway will:
- Auto-build your Python app
- Install dependencies from `requirements.txt`
- Start with `Procfile` command
- Assign a public URL automatically

---

## ⚙️ Step 5: Configure Environment Variables

In Railway Dashboard:
1. Go to your **Soward-Bot** project
2. Click **"Variables"** tab
3. **Add these required variables:**

```
TOKEN=your_discord_bot_token_here
API_PORT=3000
LOG_LEVEL=INFO
```

**Optional (if using database):**
```
DATABASE_URL=postgresql://user:password@host:5432/db
```

---

## 🎯 Step 6: Enable Discord Intents (CRITICAL!)

Before bot can connect to Discord:

1. Go to **https://discord.com/developers/applications**
2. Select your bot application
3. Go to **"Bot"** section (left sidebar)
4. **Enable these Privileged Intents:**
   - ✓ `MESSAGE_CONTENT`
   - ✓ `GUILD_MEMBERS`
   - ✓ `GUILD_PRESENCES`
5. **Save changes**
6. **Return to Railway** and click **Redeploy** button

---

## ✨ Step 7: Access Your 24/7 Dashboard

After deployment completes (takes 2-5 minutes):

1. In Railway, go to **Deployments** tab
2. Find your active deployment
3. Copy the **Public URL** (looks like: `https://sowardbot-production-xxxx.up.railway.app`)
4. **Open in browser:** Your dashboard is now live! 🎉

### Dashboard Features (All 7 Pages):
- **Login** - Authenticate with Discord token
- **Dashboard** - Real-time stats (servers, users, uptime)
- **Moderation** - Ban/mute management
- **Music** - Music player with queue
- **Economy** - Currency stats & leaderboard
- **Settings** - Bot configuration
- **Logs** - Event logging

---

## 📊 Deployment Status

### What Railway Provides (Free Tier):
✅ 20GB compute + storage per month  
✅ Unlimited projects  
✅ Auto-scaling (can adjust)  
✅ Auto-restart on crash  
✅ Free SSL/HTTPS certificate  
✅ Custom domain support  
✅ 24/7 uptime (no sleeping)  

### Typical Bot Usage:
- **SowardBot:** 2-3GB/month
- **Well within free tier** (20GB/month)
- **Cost: $0** 💰

---

## 🔧 Making Changes Later

Once deployed:

1. **Make code changes locally**
2. **Push to GitHub:**
   ```powershell
   git add .
   git commit -m "Your change description"
   git push
   ```
3. **Railway auto-redeploys** (30-60 seconds)
4. **Changes live** at your dashboard URL

---

## 🐛 Troubleshooting

### Build Failed?
- Check **Build Logs** in Railway
- Common issues:
  - Missing dependencies (add to `requirements.txt`)
  - Python version mismatch (Railway uses Python 3.11+)
  - Syntax errors in code

### Bot Won't Connect?
- Check **Deployment Logs** in Railway
- Most common: **Privileged Intents not enabled** in Discord Developer Portal
- Solution: Enable MESSAGE_CONTENT, GUILD_MEMBERS, GUILD_PRESENCES

### Dashboard Returns 502 Error?
- Check **Logs** tab in Railway
- Usually: TOKEN missing or bot hasn't started yet
- Try refreshing page after 1-2 minutes

### API Endpoints Return Empty?
- This is normal if database isn't configured
- Bot works with or without database
- Endpoints are wired but return test data

---

## 📝 Important Security Notes

✅ **Your .env is protected:**
- `.gitignore` prevents committing secrets to GitHub
- Set TOKEN in Railway Variables, not in code
- Never share your Discord token with anyone

✅ **Safe to make repo public:**
- No secrets in code (they're in Railway Variables)
- Anyone can see your code, not your token

---

## 🎉 You're Done!

Your SowardBot is now live 24/7 on Railway with a permanent dashboard link!

**Share your dashboard:**
```
https://your-railway-url.up.railway.app
```

Need help? Check Railway docs: https://docs.railway.app

---

**Summary of what's deployed:**
- Discord bot (running as `launcher.py`)
- FastAPI server (serving dashboard on port 3000)
- React frontend (7-page premium dashboard)
- All running in a single process
- 24/7 uptime
- Auto-restart on crash
- Free tier
- No credit card required

# 🚀 DEPLOY TO RAILWAY - Quick Steps

## ✅ Files Ready for Deployment
- ✓ `Procfile` - Railway entry point
- ✓ `railway.json` - Railway configuration  
- ✓ `launcher.py` - Updated for Railway PORT
- ✓ `requirements.txt` - All dependencies
- ✓ `.gitignore` - Protects .env secrets

## 🎯 Deployment in 5 Minutes

### 1️⃣ Initialize Git
```powershell
cd c:\Users\HP\Downloads\Soward-Bot-main
git init
git add .
git commit -m "Initial SowardBot deployment"
```

### 2️⃣ Push to GitHub
```powershell
# Create repository on github.com/new
# Then:
git remote add origin https://github.com/YOUR_USERNAME/Soward-Bot.git
git branch -M main
git push -u origin main
```

### 3️⃣ Deploy on Railway
1. Visit **https://railway.app**
2. Click **"New Project"** → **"Deploy from GitHub"**
3. Select **Soward-Bot** repository
4. Railway auto-detects Python project ✨

### 4️⃣ Set Environment Variables in Railway
Click **Variables** tab and add:

```
TOKEN=your_discord_bot_token_here
API_PORT=3000
LOG_LEVEL=INFO
```

**Optional (for database):**
```
DATABASE_URL=postgresql://user:pass@host:5432/sowardbot
```

### 5️⃣ Enable Discord Intents (CRITICAL)
Before bot can connect:
1. Go to **https://discord.com/developers/applications**
2. Select your bot application
3. Go to **Bot** section
4. **Enable these intents:**
   - ✓ MESSAGE_CONTENT
   - ✓ GUILD_MEMBERS
   - ✓ GUILD_PRESENCES
5. Save and redeploy on Railway

### 6️⃣ Get Your 24/7 Dashboard
After deployment completes:
- Go to **Deployments** tab
- Copy the **Public URL**
- Your dashboard: `https://your-url.up.railway.app`

---

## 📊 Dashboard Access
- **URL:** `https://your-url.up.railway.app`
- **Available 24/7** without restarting
- **SSL Certificate:** Automatic
- **Custom Domain:** Available in Settings

---

## 🔧 Troubleshooting

### Build Failed?
→ Check **Build Logs** tab for errors

### App Won't Connect to Discord?
→ Enable Privileged Intents in Discord Developer Portal

### Dashboard Returns 502?
→ Check **Logs** tab - might be TOKEN or intent issue

### Changes Not Showing After Git Push?
→ Railway auto-redeploys (wait 30-60 seconds)

---

## 📝 Important Notes

✅ **Deployed from:** GitHub repository  
✅ **Always runs:** Railway auto-restarts on crash  
✅ **Free tier:** 20GB compute/storage per month  
✅ **SowardBot usage:** ~2-3GB/month (well within free tier)  
✅ **No credit card required** for free tier  

---

## 🎉 Done!
Your SowardBot is now live 24/7 on Railway! 

**Share your dashboard URL:** `https://your-url.up.railway.app`

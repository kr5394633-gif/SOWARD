# 🚀 Railway Deployment Guide - SowardBot

## Quick Start (3 minutes)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "SowardBot deployment"
git remote add origin https://github.com/YOUR_USERNAME/Soward-Bot.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Railway
1. Go to [railway.app](https://railway.app)
2. Click **"New Project"**
3. Select **"Deploy from GitHub"**
4. Authorize GitHub and select your **Soward-Bot** repository
5. Railway will auto-detect the Python project

### Step 3: Configure Environment Variables
In Railway Dashboard, go to **Variables** and add:

```
TOKEN=your_discord_bot_token_here
DATABASE_URL=postgresql://user:password@db:5432/sowardbot
API_PORT=3000
API_HOST=0.0.0.0
LOG_LEVEL=INFO
```

> **Important:** Your Discord bot must have **Privileged Intents** enabled:
> - Go to [Discord Developer Portal](https://discord.com/developers/applications)
> - Select your bot
> - Enable: `MESSAGE_CONTENT`, `GUILD_MEMBERS`, `GUILD_PRESENCES`

### Step 4: Get Your Dashboard Link
After deployment succeeds:
1. Go to **Deployments** tab
2. Click on the active deployment
3. Copy the **Public URL** (e.g., `https://sowardbot-production.up.railway.app`)

**Your 24/7 Dashboard:** `https://sowardbot-production.up.railway.app`

---

## Advanced Configuration

### Database Setup (Optional)
If you want persistent data:
1. In Railway Dashboard, click **+ New**
2. Select **PostgreSQL**
3. Railway will auto-populate `DATABASE_URL`
4. Redeploy the application

### Custom Domain
1. Go to your Railway project → **Settings**
2. Add a custom domain (e.g., `sowardbot.your-domain.com`)
3. Point DNS to Railway nameservers

### 24/7 Uptime
- Railway auto-restarts crashed processes
- Check **Logs** tab for debugging
- Set **Restart Policy** to "Always"

### Monitoring
- **Metrics** tab: CPU, RAM, Network usage
- **Logs** tab: Real-time application output
- **Deployments** tab: Deployment history

---

## Environment Variables Reference

| Variable | Required | Example |
|----------|----------|---------|
| `TOKEN` | ✅ Yes | `MTUzNTk1NzQ0MTY2ODMyMTI5MA.GQ...` |
| `DATABASE_URL` | ❌ No | `postgresql://user:pass@host/db` |
| `API_PORT` | ❌ No | `3000` |
| `API_HOST` | ❌ No | `0.0.0.0` |
| `LOG_LEVEL` | ❌ No | `INFO` |

---

## Deployment Troubleshooting

### Build Fails
- Check **Build Logs** for errors
- Ensure `requirements.txt` has all dependencies
- Verify `Procfile` is correct

### App Won't Start
- Check **Deployment Logs**
- Verify Discord token is valid
- Enable privileged intents in Discord Developer Portal

### Dashboard Returns 502 Bad Gateway
- Check **Logs** for API startup errors
- Verify environment variables are set
- May be PostgreSQL connection issue (runs without DB, just limited)

### Zero Connections from Discord
- Check **Logs** for `PrivilegedIntentsRequired` error
- Enable intents in Discord Developer Portal
- Redeploy application

---

## Deployment Details

### What Railway Provides
- **20GB free usage/month** (CPU, RAM, storage)
- **Auto-scaling** (can adjust in Settings)
- **SSL/TLS** certificate (free, auto-renewed)
- **Custom domains** (supported)
- **Database hosting** (PostgreSQL, MySQL, Redis)

### Project Structure for Railway
```
Soward-Bot/
├── launcher.py          # Entry point (Railway runs this)
├── Procfile            # Deployment configuration
├── railway.json        # Railway settings
├── requirements.txt    # Python dependencies
├── .env                # Config (ignored in git, set in Railway)
├── api/                # FastAPI application
├── cogs/               # Discord bot extensions
├── core/               # Bot core
├── dashboard/build/    # React frontend (pre-built)
└── [other directories]
```

### First Deploy Timeline
- **0-2 min:** GitHub push
- **2-4 min:** Railway detects and starts build
- **4-8 min:** Python dependencies install
- **8-10 min:** Application starts
- **10-12 min:** Dashboard accessible

---

## After Deployment

### Access Your Bot
1. **Dashboard:** `https://your-railway-url.up.railway.app`
2. **Bot Status:** Check Logs for "Bot Ready" message
3. **API Health:** `https://your-railway-url.up.railway.app/health`

### Make Changes
1. Update code locally
2. `git push` to GitHub
3. Railway auto-redeploys (usually 30 seconds)

### Manage from CLI (Optional)
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Deploy
railway up
```

---

## Cost Estimation
- **Free tier:** 20GB compute + storage per month
- **SowardBot typical usage:** ~2-3GB/month
- **Always free:** Custom domain, SSL certificate, logs

**Your dashboard will run 24/7 completely free!** ✨

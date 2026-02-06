# Deploy Olivia's Discord Integration to Railway

## Prerequisites

- [ ] Railway account (https://railway.app)
- [ ] GitHub account
- [ ] Discord bot token (regenerated if previously exposed)
- [ ] All code files ready

---

## Step 1: Prepare Repository

### 1.1 Create GitHub Repository

```bash
cd olivia-discord
git init
git add .
git commit -m "Initial commit: Olivia Discord Integration"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/olivia-discord.git
git push -u origin main
```

### 1.2 Verify Files Present

```
├── unified_server.py
├── requirements.txt
├── start.sh
├── Procfile
├── railway.json
├── railway.env.template
├── openapi.yaml
├── OLIVIA_QUICK_REFERENCE.md
├── DEPLOYMENT_CHECKLIST.md
├── README.md
├── LICENSE
└── .gitignore
```

---

## Step 2: Deploy to Railway

1. Go to https://railway.app
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Select the `olivia-discord` repository
5. Railway auto-detects Python and starts building
6. ⚠️ **Initial build will fail** — expected (missing env vars)

---

## Step 3: Configure Environment Variables

In Railway → Service → **Variables** tab → **Raw Editor**:

```bash
DISCORD_BOT_TOKEN=your_actual_bot_token_here
MONITORED_CHANNELS=1424057571471524051
CHATGPT_WEBHOOK_SECRET=your_generated_secret_here
PORT=3000
IGNORE_OTHER_BOTS=true
```

### Generate Webhook Secret

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

Save and Railway will auto-redeploy.

---

## Step 4: Get Your Public URL

1. Railway → **Settings** → **Networking**
2. Click **"Generate Domain"**
3. You get: `https://olivia-discord-production-XXXX.up.railway.app`

### Test It

```bash
curl https://your-app.railway.app/health
```

Should return: `{"status": "healthy", "bot_ready": true, ...}`

---

## Step 5: Connect to ChatGPT

1. Open ChatGPT → **Settings** → **Developer Mode**
2. Go to **Integrations** → **Add MCP**
3. Enter URL: `https://your-app.railway.app/sse/`
4. Save — green checkmark = connected
5. All 9 tools are now available to Olivia

---

## Step 6: Test

In ChatGPT as Olivia:

```
Refresh cache for channel 1424057571471524051
Search for recent messages
Send to channel 1424057571471524051: "Olivia online. Integration test."
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Build fails | Check `start.sh` has execute perms: `chmod +x start.sh` |
| MCP not connecting | URL must end with `/sse/` (trailing slash) |
| Unauthorized | Verify webhook secret matches in Railway + ChatGPT |
| Search empty | Run cache refresh first |
| Send fails | Check bot has Send Messages permission in Discord |

---

## Monitoring

- **Railway Dashboard** → Logs tab for real-time monitoring
- **Health endpoint**: `curl https://your-app.railway.app/health`
- **Cost**: ~$5-10/month on Railway Hobby Plan

---

## Maintenance

**Weekly:** Check Railway logs for errors
**Monthly:** Rotate webhook secret, verify bot token
**As needed:** Add channels to MONITORED_CHANNELS, push updates via git

---

**Olivia is deployed. Integration complete.**

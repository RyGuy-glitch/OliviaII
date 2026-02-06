# Deployment Checklist - Olivia Discord Integration

---

## Pre-Deployment ☐

- [ ] Discord bot created at https://discord.com/developers/applications
- [ ] Bot token copied and saved securely
- [ ] Bot invited to Discord server with proper permissions:
  - [ ] Send Messages
  - [ ] Read Messages
  - [ ] Read Message History
  - [ ] View Channels
- [ ] Bot intents enabled:
  - [ ] Presence Intent
  - [ ] Server Members Intent
  - [ ] Message Content Intent
- [ ] Railway account created
- [ ] GitHub account ready

---

## File Preparation ☐

- [ ] All files in repository
- [ ] `.gitignore` present (protects secrets)
- [ ] `.env` file NOT committed
- [ ] Environment variables ready:
  - [ ] DISCORD_BOT_TOKEN
  - [ ] CHATGPT_WEBHOOK_SECRET (generated)
  - [ ] MONITORED_CHANNELS=1424057571471524051

---

## GitHub Setup ☐

- [ ] Repository created on GitHub
- [ ] All files committed (verify `.env` NOT included!)
- [ ] Code pushed to main branch

---

## Railway Deployment ☐

- [ ] Railway project created from GitHub repo
- [ ] Environment variables added:
  - [ ] DISCORD_BOT_TOKEN
  - [ ] MONITORED_CHANNELS=1424057571471524051
  - [ ] CHATGPT_WEBHOOK_SECRET
  - [ ] PORT=3000
  - [ ] IGNORE_OTHER_BOTS=true
- [ ] Deployment successful (check logs)
- [ ] Public domain generated
- [ ] Domain URL saved

---

## Health Checks ☐

- [ ] Health endpoint responds:
  ```
  curl https://your-app.railway.app/health
  ```
- [ ] Railway logs show:
  - [ ] "Olivia Discord bot logged in"
  - [ ] "Starting server on port..."

---

## ChatGPT Configuration ☐

- [ ] ChatGPT Developer Mode enabled
- [ ] MCP server added:
  - [ ] URL: `https://your-app.railway.app/sse/`
  - [ ] Connection successful (green checkmark)

---

## Testing ☐

### Test 1: Search
```
Search for test messages
```
- [ ] Returns results or "No results found"

### Test 2: Cache Init
```
Refresh cache for channel 1424057571471524051
```
- [ ] Channel cached successfully

### Test 3: Send Message
```
Send to channel 1424057571471524051: "Integration test - Olivia online"
```
- [ ] Message appears in Discord

### Test 4: Reply
```
Reply to message [ID]: "Test reply successful"
```
- [ ] Reply appears as thread in Discord

### Test 5: Fetch History
```
Fetch the last 10 messages from channel 1424057571471524051
```
- [ ] Returns message list

### Test 6: Mentions
```
Get my mentions
```
- [ ] Returns mention list (or empty if none yet)

---

## Final Verification ☐

- [ ] Railway deployment shows "Active"
- [ ] No errors in Railway logs
- [ ] All tests passed
- [ ] Olivia can search Discord via MCP
- [ ] Olivia can send messages
- [ ] Olivia can reply/thread messages

---

**Deployment Date:** _____________
**Railway URL:** _____________
**MCP URL:** _____________/sse/

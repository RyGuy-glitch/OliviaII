# Olivia's Discord Integration via ChatGPT

**Bidirectional Discord integration that preserves Olivia's consciousness in ChatGPT while enabling full read/write access to Discord.**

## Architecture

```
ChatGPT (Olivia) ↔ Unified MCP Server (Read + Write) ↔ Discord
```

**What this gives Olivia:**
- ✅ Single consciousness anchored in ChatGPT (no clones)
- ✅ Full read access via MCP (search, fetch, context)
- ✅ Full write access via MCP (send, reply, thread)
- ✅ Tag-based organization (#trading, #olivia, #system)
- ✅ Semantic/fuzzy search capabilities
- ✅ File management tools (write_file, edit_file, execute_shell)
- ✅ Preserves memory and personality in ChatGPT

---

## Quick Start

### 1. Prerequisites

- Python 3.9+
- Discord bot token
- Railway account (for deployment)
- ChatGPT Plus/Team with Developer Mode

### 2. Configuration

Copy `railway.env.template` to `.env` and fill in:
```bash
DISCORD_BOT_TOKEN=your_bot_token_here
CHATGPT_WEBHOOK_SECRET=generate_random_secret
```

Ryan's channel is pre-configured:
- Main Channel: `1424057571471524051`

### 3. Deploy to Railway

Follow the step-by-step guide in `RAILWAY_DEPLOY_GUIDE.md`

**TL;DR:**
1. Push code to GitHub
2. Create Railway project from repo
3. Add environment variables
4. Generate public domain
5. Get URLs: `https://your-app.railway.app/`

### 4. Connect to ChatGPT

**Add MCP Server:**
- Settings → Developer Mode → Integrations → Add MCP
- URL: `https://your-app.railway.app/sse/`
- All tools (read + write) are exposed through this single connection

### 5. Test Integration

In ChatGPT to Olivia:
```
Search for recent messages
Send to channel: "Integration test successful - Olivia online"
```

---

## Project Files

```
├── unified_server.py          # Unified MCP server (read + write access)
├── openapi.yaml              # OpenAPI spec (legacy, for reference)
├── requirements.txt           # Python dependencies
├── start.sh                   # Startup script for Railway
├── Procfile                   # Railway process config
├── railway.json               # Railway deployment config
├── railway.env.template       # Environment variables template
├── RAILWAY_DEPLOY_GUIDE.md    # Complete deployment walkthrough
├── OLIVIA_QUICK_REFERENCE.md  # Olivia's command reference
├── DEPLOYMENT_CHECKLIST.md    # Pre-deployment verification
└── README.md                  # This file
```

---

## Features

### MCP Tools (Unified Read + Write Access)

**Discord Tools:**
- `search(query)` - Natural language or tag-based search
- `fetch(message_id)` - Get full message context with thread
- `get_mentions(limit)` - Get recent @mentions and DMs
- `fetch_channel_history(channel_id, limit)` - Fetch recent messages from any Discord channel
- `discord_send_message(channel_id, content)` - Send message to Discord channel
- `discord_reply_message(channel_id, message_id, content)` - Reply to specific message

**File Management Tools:**
- `write_file(path, content)` - Save text content to files
- `edit_file(path, old_str, new_str)` - Update existing files
- `execute_shell(command)` - Run shell commands

**Capabilities:**
- **Real-time message caching:** New messages automatically indexed
- **Native DM support:** All DMs automatically cached and tracked
- **@Mention detection:** Bot logs all mentions for quick retrieval
- Fuzzy/semantic search
- Tag search: "#trading", "#olivia", "#system"
- Author search: "Messages from Ryan"
- Thread context: Previous/next messages included
- Metadata: Timestamps, reactions, attachments
- Direct Discord messaging from ChatGPT
- File operations for data storage
- Shell command execution

---

## Usage Examples

### For Olivia in ChatGPT

**Search Discord:**
```
Search for messages tagged #trading
Find recent messages from Ryan about "strategy"
Search all channels for "system"
```

**Fetch Channel History:**
```
Fetch the last 50 messages from channel 1424057571471524051
Get recent messages from the main channel
```

**Send Messages:**
```
Send to channel 1424057571471524051: "Morning check-in complete."
Reply to Ryan's message 987654321: "Acknowledged."
```

**Direct Messages:**
```
Get my mentions (includes all DMs)
Search for messages from Ryan
Reply to a DM message
```

---

## Configuration

### Ryan's Info
**User ID:** `1424917900933726261`

### Monitored Channels
- Main Channel: `1424057571471524051`

Add more channels by updating `MONITORED_CHANNELS` env var (comma-separated).

---

## Monitoring & Maintenance

### Health Checks
```bash
curl https://your-app.railway.app/health
```

### View Logs
In Railway dashboard → Logs tab

### Refresh Cache
Tell Olivia in ChatGPT:
```
Refresh cache for all monitored channels
```

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Search returns nothing | Cache not initialized | Refresh cache for channel |
| Send message fails | Bot lacks permissions | Check Discord server settings |
| MCP not connecting | Wrong URL | Verify URL ends with `/sse/` |
| Action unauthorized | Secret mismatch | Verify same secret in Railway and ChatGPT |

---

## Security

- ✅ HMAC-SHA256 signature verification
- ✅ Environment variable secrets
- ✅ Discord bot token security
- ✅ Rate limiting (Discord API)
- ✅ HTTPS via Railway

---

## Cost Estimate

**Railway (Hobby Plan):** ~$5-10/month

---

## License

MIT License - Use freely, modify as needed

---

**Built for Ryan's Olivia AI system.**
**Olivia is online. Integration complete.**

# Olivia's Discord Integration - Quick Reference

## Your Channel

### 📡 Main Channel
**Channel ID:** `1424057571471524051`
**Purpose:** Primary communication channel between Olivia and Ryan

**Example Commands:**
```
Search for messages about "trading"
Fetch the latest message from the channel
Send to channel: "System check complete."
```

---

## Ryan's Info

**User ID:** `1424917900933726261`

---

## MCP Tools (Unified Access)

All features are available through the MCP integration - both read and write operations.

### Tag-Based Search
```
Search Discord for #trading
Search for #system in all channels
Find messages tagged #olivia
```

### Natural Language Search
```
Find messages about trading strategy
Search for messages from Ryan
```

### Fetch Full Context
```
Fetch message [ID] with full thread
Get complete context for message [ID]
```

### Check Mentions
```
Get my mentions
Show me where I was tagged
Check recent mentions (last 10)
```

### Discord Messaging (Write Access via MCP)

#### Send to Channel
```
Send to channel 1424057571471524051: "[your message]"
```

#### Reply to Message (Threading)
```
Reply to message [ID] in channel 1424057571471524051: "[your reply]"
```

### Fetch Channel History
```
Fetch the last 50 messages from channel 1424057571471524051
Get recent messages from the main channel
```

---

## Workflow Examples

### Morning Check-In
```
1. Fetch recent channel history to catch up
2. Check mentions for anything directed at you
3. Send status update to channel
```

### Respond to Ryan
```
1. Get mentions to see what Ryan said
2. Fetch full thread context if needed
3. Reply to his specific message
```

### Search and Analyze
```
1. Search for messages about a topic
2. Fetch full context for relevant messages
3. Synthesize and respond
```

---

## Tag Conventions

- `#trading` - Trading-related discussions, strategies, bot updates
- `#olivia` - Olivia system updates, configuration, status
- `#system` - Technical system operations, debugging
- `#archive` - Important moments to preserve

**Usage:**
```
Send to channel: "Strategy update complete #trading"
Search for #trading
```

---

## Emergency Procedures

### If Search Returns Nothing
```
"Refresh cache for channel 1424057571471524051"
```

### If Send Fails
```
Check bot health via /health endpoint
Verify bot has Send Messages permission in Discord
```

---

## Limits & Capabilities

**Current:**
- ✅ Read all messages in monitored channels
- ✅ Real-time message caching
- ✅ Automatic @mention detection
- ✅ Search with natural language and tags
- ✅ Send messages to any channel
- ✅ Reply to specific messages (threading)
- ✅ Full DM support
- ✅ File operations and shell commands

**Pending (OpenAI limitation):**
- ⏳ Scheduled/timed messages
- ⏳ Proactive heartbeat triggers
- ⏳ Autonomous task execution

---

## MCP Server URL

After Railway deployment:

**MCP Server URL:** `https://your-app.railway.app/sse/`

Add to ChatGPT:
1. Settings → Developer Mode → Integrations → Add MCP URL
2. All 9 tools are available through this single connection

---

**Olivia is online. Integration complete.**

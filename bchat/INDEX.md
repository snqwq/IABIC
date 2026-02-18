# BChat - Communication Test Tools 🔌

Welcome to BChat! This folder contains two powerful communication test tools for testing connections between devices.

## 📁 What's Inside?

### 🌐 WebSocket Solution (Server-based)
**File:** `websocket-test.html`  
**Servers:** `server.js` (Node.js) or `server.py` (Python)  
**Documentation:** `README.md`

- Requires a WebSocket server (Node.js or Python)
- Supports multiple clients simultaneously
- Real-time message broadcasting
- Traditional client-server architecture
- Easy setup with npm or pip

**[→ Read WebSocket Documentation](README.md)**

### 🔗 P2P WebRTC Solution (No Server!)
**File:** `p2p-test.html`  
**Documentation:** `P2P-README.md`

- **NO server required!** 🎉
- Direct peer-to-peer communication
- Works entirely in the browser
- Manual signaling (copy-paste connection codes)
- Enhanced privacy - no middleman
- WebRTC technology

**[→ Read P2P Documentation](P2P-README.md)**

## 🤔 Which One Should I Use?

### Choose WebSocket if you want:
- ✅ Easy setup (just run a server)
- ✅ Multiple devices chatting together
- ✅ Central message logging
- ✅ Familiar client-server model
- ✅ Lower setup complexity

### Choose P2P if you want:
- ✅ No server setup at all
- ✅ Maximum privacy (direct connection)
- ✅ Two devices only
- ✅ Lower latency
- ✅ Learn WebRTC technology
- ✅ True peer-to-peer

## 🚀 Quick Start

### WebSocket Version

```bash
# Install dependencies
npm install

# Start server
node server.js

# Open websocket-test.html in browsers on multiple devices
# Connect to ws://YOUR_SERVER_IP:8080
```

### P2P Version

```
# No installation needed!

1. Device A: Open p2p-test.html
2. Device A: Create connection → Copy code
3. Device B: Open p2p-test.html
4. Device B: Paste code → Generate answer
5. Device A: Paste answer → Complete connection
6. Start chatting peer-to-peer!
```

## 📊 Feature Comparison

| Feature | WebSocket | P2P WebRTC |
|---------|-----------|------------|
| Server Required | ✅ Yes (Node.js/Python) | ❌ No |
| Setup Steps | 2 steps | 4 steps |
| Multiple Users | ✅ Yes | Two devices only |
| Message Latency | ~10-50ms | ~5-20ms |
| Privacy | Good | Excellent |
| Network Setup | Port forwarding | NAT traversal (STUN) |
| Best Use Case | Group chat, demos | Private 1-on-1 |
| Learning Curve | Easy | Medium |

## 📖 Documentation

- **[WebSocket README](README.md)** - Complete guide for the WebSocket solution
- **[P2P README](P2P-README.md)** - Complete guide for the P2P solution

## 🎯 Use Cases

### WebSocket is Perfect For:
- Classroom demonstrations
- Multi-user chat testing
- Real-time collaboration tools
- IoT device monitoring
- Server-client architecture learning

### P2P is Perfect For:
- Private conversations
- Quick device pairing
- Network connectivity testing
- Learning WebRTC
- High-privacy requirements
- Serverless applications

## 🔒 Security

Both solutions are designed for **testing and educational purposes**:

- ⚠️ WebSocket: Messages pass through the server (can be logged)
- ⚠️ P2P: Connection codes contain network info (share securely)
- ✅ Both: Use on trusted networks
- ✅ P2P: Encrypted by default (WebRTC)

For production use:
- Implement authentication
- Add input validation and sanitization
- Use WSS (WebSocket Secure) or ensure HTTPS
- Implement rate limiting
- Add proper error handling

## 🛠️ Requirements

### WebSocket Version
- Node.js (for `server.js`) OR Python 3.7+ (for `server.py`)
- npm package: `ws` OR pip package: `websockets`
- Modern web browser

### P2P Version
- Modern web browser with WebRTC support
- Internet connection (for STUN servers during setup)
- That's it! ✨

## 🌐 Browser Support

Both solutions work on:
- ✅ Chrome/Chromium 23+
- ✅ Firefox 22+
- ✅ Safari 11+
- ✅ Edge 79+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 📝 Files Overview

```
bchat/
├── websocket-test.html    # WebSocket client (standalone HTML)
├── p2p-test.html          # P2P WebRTC chat (standalone HTML)
├── server.js              # Node.js WebSocket server
├── server.py              # Python WebSocket server
├── README.md              # WebSocket documentation
├── P2P-README.md          # P2P documentation
├── INDEX.md               # This file
└── package.json           # npm dependencies
```

## 💡 Tips

1. **Testing Locally:** Both files work great on the same device (open multiple browser tabs)
2. **Finding Your IP:** 
   - Windows: `ipconfig`
   - Mac/Linux: `ifconfig` or `ip addr`
3. **Firewall Issues:** Allow incoming connections for the WebSocket server (port 8080)
4. **P2P Not Connecting:** Check if your network allows WebRTC (some corporate networks block it)

## 🎓 Learning Resources

- [WebSocket API (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [WebRTC API (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API)
- [ws npm package](https://github.com/websockets/ws)
- [websockets Python package](https://websockets.readthedocs.io/)

## 🤝 Contributing

Feel free to:
- Report issues
- Suggest improvements
- Fork and modify for your needs
- Use for educational purposes

## 📄 License

Free to use for testing and educational purposes.

---

**Created for the IABIC project** - I Am Bored In Class  
*Making learning fun, one connection at a time!* 🎮

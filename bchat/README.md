# WebSocket Connection Test

A standalone HTML-based WebSocket test tool for testing connections between two devices on the same network.

## 📁 Files

- **websocket-test.html** - Standalone HTML file with WebSocket client functionality
- **server.js** - Node.js WebSocket server (optional)
- **server.py** - Python WebSocket server (optional)

## 🚀 Quick Start

### Method 1: Using Node.js Server (Recommended)

1. **Install Node.js** (if not already installed): [https://nodejs.org/](https://nodejs.org/)

2. **Install the WebSocket library**:
   ```bash
   npm install ws
   ```

3. **Start the server**:
   ```bash
   node server.js
   ```

4. **Find your IP address**:
   - Windows: Open Command Prompt and run `ipconfig`
   - Mac/Linux: Open Terminal and run `ifconfig` or `ip addr`
   - Look for your local network IP (usually starts with 192.168.x.x or 10.x.x.x)

5. **Open the HTML file**:
   - On the server device: Open `websocket-test.html` in a web browser
   - On other devices: Copy `websocket-test.html` to those devices and open in a browser

6. **Connect**:
   - Switch to "Client Mode"
   - Enter the server URL:
     - Same device: `ws://localhost:8080`
     - Other devices: `ws://YOUR_SERVER_IP:8080` (replace YOUR_SERVER_IP with actual IP)
   - Click "Connect to Server"

7. **Start chatting**:
   - Type messages and press Send or Enter
   - Messages will be broadcasted to all connected clients

### Method 2: Using Python Server

1. **Install Python 3.7+** (if not already installed): [https://www.python.org/](https://www.python.org/)

2. **Install the websockets library**:
   ```bash
   pip install websockets
   ```

3. **Start the server**:
   ```bash
   python server.py
   ```

4. **Follow steps 4-7 from Method 1**

## 🌐 Testing Between Two Devices

### Setup:
1. Make sure both devices are on the same network (same WiFi)
2. On Device A (Server):
   - Start the WebSocket server (using Node.js or Python)
   - Note the IP address of this device
3. On Device B (Client):
   - Open `websocket-test.html` in a browser
   - Switch to "Client Mode"
   - Enter `ws://DEVICE_A_IP:8080`
   - Click Connect

### Multiple Devices:
- You can connect multiple devices to the same server
- All messages will be broadcasted to all connected clients
- Each device will see messages from all other devices

## 🔧 Troubleshooting

### Cannot connect to server:
- Verify the server is running
- Check the IP address is correct
- Ensure both devices are on the same network
- Check if firewall is blocking port 8080
- Try using `http://` instead of `https://` when opening the HTML file

### "Connection refused" error:
- Make sure the WebSocket server is running
- Check if port 8080 is already in use by another application
- Try a different port (edit both server and client URL)

### Firewall issues:
- Windows: Allow Node.js/Python through Windows Firewall
- Mac: System Preferences → Security & Privacy → Firewall → Allow incoming connections
- Router: Port 8080 should be open for local network (usually is by default)

## 📱 Standalone HTML Features

The `websocket-test.html` file is completely standalone and includes:

- ✅ No external dependencies
- ✅ Works offline (once loaded)
- ✅ Modern, responsive UI
- ✅ Real-time message display
- ✅ Connection status indicators
- ✅ Timestamp for each message
- ✅ Server setup instructions included
- ✅ Auto-scrolling chat interface
- ✅ Dark code snippets for easy reading

## 🎯 Use Cases

- Testing WebSocket connectivity between devices
- Debugging network issues
- Learning WebSocket protocol
- Quick peer-to-peer messaging
- Network classroom demonstrations
- IoT device communication testing

## 📝 Technical Details

- **Protocol**: WebSocket (RFC 6455)
- **Default Port**: 8080
- **Message Format**: Plain text
- **Broadcast**: All messages are sent to all connected clients
- **Browser Support**: All modern browsers (Chrome, Firefox, Safari, Edge)

## 🔒 Security Note

This is a test tool intended for use on trusted local networks. For production use:
- Use WSS (WebSocket Secure) instead of WS
- Implement authentication
- Validate and sanitize all messages
- Use proper CORS configuration
- Implement rate limiting

## 📜 License

Feel free to use and modify these files for testing and educational purposes.

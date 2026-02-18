// Simple WebSocket Server for Testing
// Install dependencies: npm install ws
// Run: node server.js

const WebSocket = require('ws');
const server = new WebSocket.Server({ port: 8080 });

console.log('╔════════════════════════════════════════════════╗');
console.log('║   WebSocket Test Server Running on Port 8080  ║');
console.log('╚════════════════════════════════════════════════╝');
console.log('');
console.log('📡 Server is ready to accept connections');
console.log('🔗 Connect from clients using: ws://YOUR_IP:8080');
console.log('💻 For same device use: ws://localhost:8080');
console.log('');
console.log('To find your IP address:');
console.log('  - Windows: ipconfig');
console.log('  - Mac/Linux: ifconfig or ip addr');
console.log('');

let clientCounter = 0;

server.on('connection', (ws, req) => {
    const clientId = ++clientCounter;
    const clientIp = req.socket.remoteAddress;
    
    console.log(`✅ Client #${clientId} connected from ${clientIp}`);
    console.log(`   Total clients: ${server.clients.size}`);
    
    // Send welcome message
    ws.send(JSON.stringify({
        type: 'system',
        message: `Welcome! You are client #${clientId}. Total clients: ${server.clients.size}`
    }));
    
    ws.on('message', (message) => {
        const messageStr = message.toString();
        console.log(`📨 Message from Client #${clientId}: ${messageStr}`);
        
        // Broadcast to all clients
        let broadcastCount = 0;
        server.clients.forEach((client) => {
            if (client.readyState === WebSocket.OPEN) {
                client.send(messageStr);
                broadcastCount++;
            }
        });
        
        console.log(`   ↳ Broadcasted to ${broadcastCount} client(s)`);
    });
    
    ws.on('close', () => {
        console.log(`❌ Client #${clientId} disconnected`);
        console.log(`   Total clients: ${server.clients.size}`);
    });
    
    ws.on('error', (error) => {
        console.error(`⚠️  Error with Client #${clientId}:`, error.message);
    });
});

server.on('error', (error) => {
    console.error('❌ Server error:', error);
});

// Graceful shutdown
process.on('SIGINT', () => {
    console.log('\n\n🛑 Shutting down server...');
    server.close(() => {
        console.log('✅ Server closed successfully');
        process.exit(0);
    });
});

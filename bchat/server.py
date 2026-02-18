#!/usr/bin/env python3
"""
Simple WebSocket Server for Testing
Install dependencies: pip install websockets
Run: python server.py
"""

import asyncio
import websockets
import json
from datetime import datetime

clients = set()
client_counter = 0

async def handler(websocket, path):
    # path parameter is required by websockets.serve but not used in this simple handler
    global client_counter
    client_counter += 1
    client_id = client_counter
    
    clients.add(websocket)
    client_ip = websocket.remote_address[0]
    
    print(f"✅ Client #{client_id} connected from {client_ip}")
    print(f"   Total clients: {len(clients)}")
    
    try:
        # Send welcome message
        welcome_msg = json.dumps({
            "type": "system",
            "message": f"Welcome! You are client #{client_id}. Total clients: {len(clients)}"
        })
        await websocket.send(welcome_msg)
        
        # Handle messages
        async for message in websocket:
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"📨 [{timestamp}] Message from Client #{client_id}: {message}")
            
            # Broadcast to all clients
            broadcast_count = 0
            disconnected = set()
            
            for client in clients:
                try:
                    await client.send(message)
                    broadcast_count += 1
                except websockets.exceptions.ConnectionClosed:
                    disconnected.add(client)
            
            # Remove disconnected clients
            clients.difference_update(disconnected)
            
            print(f"   ↳ Broadcasted to {broadcast_count} client(s)")
    
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        clients.discard(websocket)
        print(f"❌ Client #{client_id} disconnected")
        print(f"   Total clients: {len(clients)}")

async def main():
    print("╔════════════════════════════════════════════════╗")
    print("║   WebSocket Test Server Running on Port 8080  ║")
    print("╚════════════════════════════════════════════════╝")
    print()
    print("📡 Server is ready to accept connections")
    print("🔗 Connect from clients using: ws://YOUR_IP:8080")
    print("💻 For same device use: ws://localhost:8080")
    print()
    print("To find your IP address:")
    print("  - Windows: ipconfig")
    print("  - Mac/Linux: ifconfig or ip addr")
    print()
    
    async with websockets.serve(handler, "0.0.0.0", 8080):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down server...")
        print("✅ Server closed successfully")

import asyncio
import json

from fastapi import WebSocket

from app import app


@app.websocket("/ws/chats")
async def start_chat_websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(5)
        data = await websocket.receive_text()
        data = json.loads(data)


@app.websocket("/ws/messages")
async def start_chat_websocket(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(5)
        data = await websocket.receive_text()
        data = json.loads(data)

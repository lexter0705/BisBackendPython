import asyncio
import json

from fastapi import WebSocket, APIRouter

router = APIRouter(prefix="/ws")


@router.websocket("/chats/{user_id}")
async def start_chats_connection(websocket: WebSocket, user_id: str):
    await websocket.accept()
    while True:
        await asyncio.sleep(5)
        data = await websocket.receive_text()
        data = json.loads(data)
        print(data)


@router.websocket("/messages/{user_id}")
async def start_messages_connection(websocket: WebSocket, user_id: str):
    await websocket.accept()
    while True:
        await asyncio.sleep(5)
        data = await websocket.receive_text()
        data = json.loads(data)
        print(data)
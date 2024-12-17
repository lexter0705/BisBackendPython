import asyncio
import json

from fastapi import WebSocket, APIRouter

from server.base_includer import chat_worker, user_worker

router = APIRouter(prefix="/chats")


def form_chats(chats: list[tuple], user_chat_id: str) -> dict:
    returned = {"type": "chats", "chats": []}
    for i in chats:
        chat_name = i[1] if i[1] != user_chat_id else i[2]
        returned["chats"].append({"chat_id": i[0], "chat_name": chat_name})
    return returned


@router.websocket("/{user_id}")
async def start_chats_connection(user_id: str, websocket: WebSocket):
    await websocket.accept()
    current_chats_count = 0
    while True:
        chats = chat_worker.get_user_chats(user_id)
        if current_chats_count < len(chats):
            current_chats_count = len(chats)
            await websocket.send_json(form_chats(chats, user_id))
        await asyncio.sleep(20)

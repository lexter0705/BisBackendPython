import asyncio
import json
from time import gmtime, strftime

from fastapi import WebSocket, APIRouter

from server.base_includer import messages_worker

router = APIRouter(prefix="/messages")


def form_messages(messages: list[tuple]) -> dict:
    returned = {"type": "messages", "messages": []}
    for i in messages:
        returned["messages"].append({"userId": i[1], "messageText": i[3]})
    print(returned)
    return returned


@router.websocket("/{chat_id}")
async def start_messages_connection(chat_id: int, websocket: WebSocket):
    await websocket.accept()
    current_messages_count = 0
    while True:
        messages = messages_worker.select_all_messages_in_chat(chat_id)
        if current_messages_count < len(messages):
            current_messages_count = len(messages)
            await websocket.send_json(form_messages(messages))
        data = await websocket.receive_text()
        if data:
            data = json.loads(data)
            data["chat_id"] = chat_id
            data["time"] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            messages_worker.insert_new_row(data)
        await asyncio.sleep(5)

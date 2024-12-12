from fastapi import FastAPI

from database.workers.chat import ChatWorker
from database.workers.message import MessageWorker
from database.workers.user import UserWorker

app = FastAPI()
chat_worker = ChatWorker("../database/main.db")
messages_worker = MessageWorker("../database/main.db")
user_worker = UserWorker("../database/main.db")

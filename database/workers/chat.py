from sqlalchemy import select, or_

from database.creator import ChatTable
from database.worker import DatabaseWorker


class ChatWorker(DatabaseWorker):
    def __init__(self, database_path: str):
        super().__init__(ChatTable, database_path)

    def get_user_chats(self, user_address: str):
        data = self.connect.execute(select(ChatTable).where(
            or_(ChatTable.first_user_id == user_address, ChatTable.second_user_id == user_address)))

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from server.hendlers.post_http import router as http_router
from server.hendlers.websocket import router as websocket_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(http_router)
app.include_router(websocket_router)

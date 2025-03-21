from typing import List

from pydantic import BaseModel
from starlette.websockets import WebSocket


class ConnectionManagerService:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.active_processing_requests: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def _disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    @staticmethod
    async def send(message: BaseModel, websocket: WebSocket):
        await websocket.send_text(message.model_dump_json())

    async def _broadcast(self, message: BaseModel):
        for connection in self.active_connections:
            await connection.send_text(message.model_dump_json())

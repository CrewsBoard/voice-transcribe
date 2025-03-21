from fastapi import APIRouter
from starlette.websockets import WebSocket

from voice_transcribe.controllers import BaseController


class WsController(BaseController):
    def __init__(self):
        super().__init__()
        self.router = APIRouter()

        self.router.add_websocket_route("/ws", self.transcribe)

    async def transcribe(self, websocket: WebSocket) -> None:
        await self.ws_service.init(websocket, self.get_service_data)

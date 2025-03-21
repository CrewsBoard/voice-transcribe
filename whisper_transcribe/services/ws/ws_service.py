from starlette.websockets import WebSocket, WebSocketDisconnect
from whisper_transcribe.dtos.core import RequestMethods

from whisper_transcribe.services.ws import ConnectionManagerService
from whisper_transcribe.shared.utils import logger


class WsService(ConnectionManagerService):
    def __init__(self):
        super().__init__()

    async def init(self, websocket: WebSocket, processor_callback: callable) -> None:
        await self.connect(websocket)
        await self.process(websocket, processor_callback)

    async def process(self, websocket: WebSocket, processor_callback: callable) -> None:
        try:
            while True:
                data = await websocket.receive_json()
                process_data = await processor_callback(data)
                await self.send(message=process_data, websocket=websocket)
        except WebSocketDisconnect as e:
            logger.info(f"Client disconnected: {e}")
            self._disconnect(websocket)
        except Exception as e:
            logger.error(f"Error in WebSocket connection: {e}")
            self._disconnect(websocket)

from typing import Any

from voice_transcribe.services.ws import WsService


class BaseService:
    def __init__(self):
        self.ws_service = WsService()

    @classmethod
    async def get_service_data(cls, data: Any) -> Any:
        pass

from pydantic import BaseModel

from voice_transcribe.dtos.ws import WsRequestTypes


class WsResponseDto(BaseModel):
    type: WsRequestTypes
    error: str = None

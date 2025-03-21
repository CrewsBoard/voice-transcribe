from pydantic import BaseModel

from whisper_transcribe.dtos.ws import WsRequestTypes


class WsResponseDto(BaseModel):
    type: WsRequestTypes
    error: str = None

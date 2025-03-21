from pydantic import UUID4

from voice_transcribe.dtos.ws import WsResponseDto


class TranscribedDto(WsResponseDto):
    id: UUID4
    text: bytes
    language: str
    timestamp: float
    duration: float
    token_count: float

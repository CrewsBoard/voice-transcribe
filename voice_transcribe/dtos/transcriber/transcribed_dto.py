from pydantic import UUID4

from voice_transcribe.dtos.ws import WsResponseDto


class TranscribedDto(WsResponseDto):
    id: UUID4
    text: str
    language: str
    timestamp: float
    duration: float
    processing_time: float
    token_count: float

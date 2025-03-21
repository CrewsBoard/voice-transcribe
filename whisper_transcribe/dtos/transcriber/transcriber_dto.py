from pydantic import UUID4

from whisper_transcribe.dtos.ws import WsRequestDto


class TranscriberDto(WsRequestDto):
    id: UUID4
    audio: bytes

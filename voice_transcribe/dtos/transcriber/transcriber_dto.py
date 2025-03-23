from typing import List

from pydantic import UUID4

from voice_transcribe.dtos.ws import WsRequestDto


class TranscriberDto(WsRequestDto):
    id: UUID4
    audio: List[float]
    sample_rate: int

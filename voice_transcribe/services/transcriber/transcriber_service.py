import datetime

from pydantic import UUID4

from voice_transcribe.dtos.transcriber import TranscriberDto, TranscribedDto
from voice_transcribe.services.core.base_service import BaseService
from voice_transcribe.shared.utils import logger


class TranscriberService(BaseService):
    def __init__(self):
        super().__init__()
        self.transcriber_counter: dict[UUID4, int] = {}

    def _increment_counter(self, _id: UUID4):
        if _id not in self.transcriber_counter:
            self.transcriber_counter[_id] = 0
        self.transcriber_counter[_id] += 1

    async def get_service_data(self, data: TranscriberDto) -> TranscribedDto:
        logger.info(f"Transcribing {data.id}")
        chunk_name = f"{data.id}_{self.transcriber_counter.get(data.id, 0)}"
        await self.save_audio_chunk(data.audio, chunk_name, data.sample_rate)
        self._increment_counter(data.id)
        d = {
            "id": data.id,
            "type": data.type,
            "text": "rafsun".encode("utf-8"),
            "language": "en",
            "timestamp": datetime.datetime.now(datetime.timezone.utc).timestamp(),
            "duration": 0,
            "token_count": 0,
        }
        return TranscribedDto.model_validate(d)

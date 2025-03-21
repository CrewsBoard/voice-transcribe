import datetime

from whisper_transcribe.dtos.transcriber import TranscriberDto, TranscribedDto
from whisper_transcribe.services.core.base_service import BaseService
from whisper_transcribe.shared.utils import logger


class TranscriberService(BaseService):
    async def get_service_data(self, data: TranscriberDto) -> TranscribedDto:
        logger.info(f"Transcribing {data.id}")
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

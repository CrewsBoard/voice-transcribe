import datetime

from pydantic import UUID4

from voice_transcribe.dtos.models.model_names import ModelNames
from voice_transcribe.dtos.models.model_sizes import ModelSizes
from voice_transcribe.dtos.transcriber import TranscriberDto, TranscribedDto
from voice_transcribe.services.core.base_service import BaseService
from voice_transcribe.services.model import ModelService
from voice_transcribe.shared.utils import logger


class TranscriberService(BaseService):
    def __init__(self, model_service: ModelService):
        super().__init__()
        self.model_service = model_service
        self.model = self.model_service.model
        self.transcriber_counter: dict[UUID4, int] = {}

    def _increment_counter(self, _id: UUID4):
        if _id not in self.transcriber_counter:
            self.transcriber_counter[_id] = 0
        self.transcriber_counter[_id] += 1

    async def get_service_data(self, data: TranscriberDto) -> TranscribedDto:
        logger.info(f"Transcribing {data.id}")
        model = self.model[ModelNames(data.model.name)][ModelSizes(data.model.size)]
        chunk_name = f"{data.id}_{self.transcriber_counter.get(data.id, 0)}"
        audio_array, _ = self.process_audio_array(data.audio)
        audio_file = await self.save_audio_chunk(audio_array, chunk_name, data.sample_rate)
        start_time = datetime.datetime.now()
        if data.model.name == ModelNames.WHISPER:
            transcription = model.transcribe(audio=audio_file)
            transcribed_text = transcription['text']
            transcribed_language = transcription['language']
        else:
            raise Exception(f"Model {data.model.name} not supported")
        end_time = datetime.datetime.now()
        processing_time = (end_time - start_time).total_seconds()
        self._increment_counter(data.id)
        transcribed_data = {
            "id": data.id,
            "type": data.type,
            "text": transcribed_text,
            "language": transcribed_language,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).timestamp(),
            "duration": 0,
            "processing_time": processing_time,
            "token_count": 0,
        }
        logger.info(f"Process finished for {data.id}")
        await self.delete_audio_chunk(chunk_name)
        return TranscribedDto.model_validate(transcribed_data)

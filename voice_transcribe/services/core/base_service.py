import os
import wave
from pathlib import Path
from typing import Any, List, Tuple

import numpy as np

from voice_transcribe.shared.utils import logger


class BaseService:
    def __init__(self):
        self.tmp_chunk_dir = os.path.join('..', '.tmp')

    @classmethod
    async def get_service_data(cls, data: Any) -> Any:
        pass

    @staticmethod
    def process_audio_array(audio_array: List[float]) -> Tuple[np.ndarray, np.ndarray]:
        audio_array = np.array(audio_array, dtype=np.float32)
        pcm_data = (audio_array * 32767).astype(np.int16)
        return audio_array, pcm_data

    async def save_audio_chunk(self, audio_data, chunk_name, sample_rate):
        audio_array, pcm_data = self.process_audio_array(audio_data)

        Path(self.tmp_chunk_dir).mkdir(parents=True, exist_ok=True)
        output_file = os.path.abspath(os.path.join(self.tmp_chunk_dir, f"chunk_{chunk_name}.wav"))

        with wave.open(output_file, 'wb') as wav_file:
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 16-bit
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(pcm_data.tobytes())

        logger.info(f"Saving chunk {chunk_name} to {output_file}")
        return output_file

    async def delete_audio_chunk(self, chunk_name):
        chunk_path = os.path.join(self.tmp_chunk_dir, f"chunk_{chunk_name}.wav")
        if os.path.exists(chunk_path):
            os.remove(chunk_path)
            logger.info(f"Deleted chunk {chunk_name} from {chunk_path}")
        else:
            logger.warning(f"Chunk {chunk_name} not found at {chunk_path}")

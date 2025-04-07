import logging
import os
from pathlib import Path
from typing import Any

import whisper

from voice_transcribe.dtos.models.model_names import ModelNames
from voice_transcribe.dtos.models.model_sizes import ModelSizes
from voice_transcribe.services.core import settings


class ModelService:
    def __init__(self):
        self.model: dict[ModelNames, dict[ModelSizes, Any]] = {}
        self._download_dir()
        self._download_model()

    def _download_dir(self) -> None:
        self.download_dir = os.path.abspath(settings.model.model_store_path)
        Path(self.download_dir).mkdir(parents=True, exist_ok=True)

    def _download_model(self):
        for model in ModelNames:
            if model == ModelNames.WHISPER:
                self.model[model] = {}
                for size in ModelSizes:
                    self.model[model][size] = whisper.load_model(name=size.value, download_root=self.download_dir)
                    logging.warn(f"Model {model} {size} loaded successfully from {self.download_dir}")

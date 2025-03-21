from fastapi.routing import APIRouter

from whisper_transcribe.controllers import TranscribeController

routes: list[APIRouter] = [
    TranscribeController().router
]

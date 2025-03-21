from fastapi import APIRouter

from whisper_transcribe.controllers import BaseController


class TranscribeController(BaseController):
    def __init__(self):
        super().__init__()
        self.router = APIRouter(tags=self.transcribe_swagger_tags)

        self.router.add_api_route("/transcribe", self.transcribe, methods=["POST"])

    @staticmethod
    async def transcribe() -> dict[str, str]:
        return {
            "message": "Transcribe successful"
        }

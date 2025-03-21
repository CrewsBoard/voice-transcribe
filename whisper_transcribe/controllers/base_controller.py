from typing import Any

from whisper_transcribe.dtos.core import RequestMethods

from whisper_transcribe.dtos.transcriber import TranscriberDto
from whisper_transcribe.dtos.ws import WsRequestTypes
from whisper_transcribe.services.core.base_service import BaseService
from whisper_transcribe.services.transcriber import TranscriberService
from whisper_transcribe.services.ws import WsService


class BaseController():
    def __init__(self):
        self.transcribe_swagger_tags = ["Transcribe"]

        self.ws_swagger_tags = ["ws"]
        self.ws_service = WsService()
        self.transcriber_service = TranscriberService()

    async def get_service_data(self, data: dict[str, Any]) -> Any:
        service: BaseService
        service_param: WsRequestTypes
        service_type = WsRequestTypes(data.get("type"))
        match service_type:
            case WsRequestTypes.TRANSCRIBE:
                service_param = TranscriberDto.model_validate(data)
                service = self.transcriber_service
        if not isinstance(service, BaseService):
            raise Exception(f"Invalid service type {service_type}")
        return await service.get_service_data(data=service_param)

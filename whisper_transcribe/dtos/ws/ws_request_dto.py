from pydantic import BaseModel

from .ws_request_types import WsRequestTypes


class WsRequestDto(BaseModel):
    type: WsRequestTypes

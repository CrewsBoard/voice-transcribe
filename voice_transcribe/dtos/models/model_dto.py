from pydantic import BaseModel

from .model_names import ModelNames
from .model_sizes import ModelSizes


class ModelDto(BaseModel):
    name: ModelNames
    size: ModelSizes

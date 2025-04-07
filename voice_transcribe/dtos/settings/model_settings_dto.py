from pydantic import BaseModel


class ModelSettingsDto(BaseModel):
    model_store_path: str

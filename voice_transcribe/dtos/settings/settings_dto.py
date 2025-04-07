from voice_transcribe.dtos.settings import ServerSettingsDto, ModelSettingsDto


class SettingsDto:
    settings_type: str
    settings_dir: str
    server: ServerSettingsDto
    model: ModelSettingsDto

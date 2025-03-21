from whisper_transcribe.dtos.settings import ServerSettingsDto


class SettingsDto:
    settings_type: str
    settings_dir: str
    server: ServerSettingsDto

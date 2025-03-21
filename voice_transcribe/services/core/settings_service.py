import os
from pathlib import Path

import yaml
from pydantic_settings import BaseSettings
from voice_transcribe.dtos.settings import SettingsDto


class SettingsService(BaseSettings, SettingsDto):

    @classmethod
    def settings_customise_sources(cls, settings_cls, init_settings, env_settings, dotenv_settings,
                                   file_secret_settings):
        return cls.yaml_config_source(), env_settings, init_settings, file_secret_settings

    @classmethod
    def yaml_config_source(cls):
        _project_name = 'voice_transcribe'
        _default_env = 'dev'
        _config_dir = 'configs'
        _config_extension = '.yaml'
        _os_env_variable = 'ENVIRONMENT'

        settings_type: str = os.environ.get(_os_env_variable, _default_env)
        project_path = os.path.abspath(__file__).split(_project_name)
        project_path = project_path[:-1][0]
        settings_dir = os.path.join(project_path, _project_name, _config_dir)
        settings_path = os.path.join(settings_dir, f"{settings_type}{_config_extension}")
        config_path = Path(settings_path)
        if config_path.exists():
            with config_path.open("r") as f:
                data = yaml.safe_load(f)
            data["settings_type"] = settings_type
            data["settings_dir"] = settings_dir
            return lambda: data
        return lambda: {}

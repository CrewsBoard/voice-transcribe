from fastapi import FastAPI

from whisper_transcribe.routers import routes
from whisper_transcribe.shared.utils import logger


class BootstrapperService:
    @staticmethod
    async def start(app: FastAPI):
        logger.warn("Starting application...")
        for route in routes:
            app.include_router(route)
        logger.warn("Application started.")

    @staticmethod
    async def stop(app: FastAPI):
        logger.warn("Stopping application...")
        logger.warn("Application stopped.")

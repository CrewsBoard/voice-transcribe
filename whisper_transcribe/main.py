import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from whisper_transcribe.routers import routes


def create_app():
    app = FastAPI(docs_url="/docs", redoc_url="/redoc",
                  swagger_ui_parameters={"syntaxHighlight": {"theme": "obsidian"}})
    origins = ["*"]
    for route in routes:
        app.include_router(route)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


if __name__ == "__main__":
    server_config = uvicorn.Config(app=create_app(), host="0.0.0.0", port=8000, reload=True)
    server = uvicorn.Server(server_config)
    server.run()

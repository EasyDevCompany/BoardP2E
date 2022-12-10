from app.api.api_v1 import api
from app.api import deps
from fastapi import FastAPI, Response
from app.core.config import settings
from app.core.containers import Container
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1.endpoints import user_auth
from fastapi.staticfiles import StaticFiles



def create_app():
    container = Container()
    container.wire(modules=[deps, user_auth])
    fastapi_app = FastAPI(
        title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )
    fastapi_app.container = container

    fastapi_app.include_router(api.api_router, prefix=settings.API_V1_STR)
    # fastapi_app.mount("/static", StaticFiles(directory="static"), name="static")
    return fastapi_app


app = create_app()

from fastapi import FastApi

from store.core.config import settings
from store.routers import api_router

class App(FastApi):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args, 
            **kwargs, 
            version="0.0.1",
            title=settings.PROJECT_NAME,
            rooth_path=settings.ROOT_PATH
        )


app = App()
app.include_router(api_router)
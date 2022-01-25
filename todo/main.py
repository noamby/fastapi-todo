from fastapi import APIRouter, FastAPI

from todo.containers import Container
from todo.modules.task import endpoints

container = Container()

routes = APIRouter(prefix="/v1")
routes.include_router(endpoints.routes)

app = FastAPI(title=container.settings.app_title())
app.container = container  # type: ignore
app.include_router(routes)  # type: ignore

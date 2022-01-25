from dependency_injector import containers, providers

from todo import settings
from todo.infrastructure.cache import CacheClient
from todo.modules.task.containers import TaskContainer


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[".modules.task.endpoints"]
    )

    settings = providers.Configuration(pydantic_settings=[settings.Settings()])
    cache = providers.Resource(
        CacheClient,
        host=settings.redis_host,
        port=settings.redis_port,
        password=settings.redis_password,
    )

    task = providers.Container(TaskContainer, cache=cache)

from dependency_injector import containers, providers

from todo.modules.task.repositories import InMemoryTaskRepo
from todo.modules.task.services import CompleteTask, CreateTask, ListTasks


class TaskContainer(containers.DeclarativeContainer):
    cache: providers.Dependency = providers.Dependency()

    task_repo = providers.Factory(InMemoryTaskRepo, cache=cache)

    create_task_service = providers.Factory(CreateTask, task_repo=task_repo)
    complete_task_service = providers.Factory(CompleteTask, task_repo=task_repo)
    list_tasks_service = providers.Factory(ListTasks, task_repo=task_repo)

from typing import Dict, List

from dependency_injector.wiring import Provide

from todo.infrastructure.cache import CacheClient
from todo.modules.task.entities import Task
from todo.modules.task.exceptions import TaskNotFoundException
from todo.modules.task.repository_interfaces import TaskRepoInterface


class InMemoryTaskRepo(TaskRepoInterface):
    tasks: Dict[str, Task] = {}
    cache: CacheClient = Provide["cache"]

    def __init__(self, cache: CacheClient):
        self.cache = cache

    def find(self, id: str) -> Task:
        task = self.tasks.get(id)
        if not task:
            raise TaskNotFoundException(f"Task {id} was not found")
        return task

    # This will work with DI, cache is of type CacheClient
    # def list(self) -> List[Task]:
    #     results = self.cache.get("ALL_TASKS")
    #
    #     if not results:
    #         print("cache miss")
    #         results = list(self.tasks.values())
    #         self.cache.set("ALL_TASKS", results)
    #
    #     return results

    @cache.cache_on_arguments(expiration_time=60)
    def list(self) -> List[Task]:
        return list(self.tasks.values())

    def create(self, task: Task):
        self.tasks[task.id] = task

    def update(self, task: Task):
        self.tasks[task.id] = task

    def delete(self, id: str):
        self.tasks.pop(id)

    def uncompleted_tasks(self) -> List[Task]:
        tasks = list(self.tasks.values())
        return list(filter(lambda t: not t.completed, tasks))

    def completed_tasks(self) -> List[Task]:
        tasks = list(self.tasks.values())
        return list(filter(lambda t: t.completed, tasks))

from typing import List, Protocol

from todo.modules.task.entities import Task


class BaseRepoInterface(Protocol):
    def find(self, id):
        pass

    def list(self):
        pass

    def create(self, entity):
        pass

    def update(self, entity):
        pass

    def delete(self, id):
        pass


class TaskRepoInterface(BaseRepoInterface, Protocol):
    def uncompleted_tasks(self) -> List[Task]:
        pass

    def completed_tasks(self) -> List[Task]:
        pass

from typing import List, Optional

from todo.modules.task.dtos import CreateTaskDTO, TaskDTO
from todo.modules.task.entities import Task
from todo.modules.task.repository_interfaces import TaskRepoInterface


class CreateTask:
    def __init__(self, task_repo: TaskRepoInterface):
        self.task_repo = task_repo

    def execute(self, create_task_dto: CreateTaskDTO) -> TaskDTO:
        task = Task.build(**create_task_dto.dict())
        self.task_repo.create(task)
        return TaskDTO.from_entity(task)


class ListTasks:
    def __init__(self, task_repo: TaskRepoInterface):
        self.task_repo = task_repo

    def execute(self, completed: Optional[bool]) -> List[TaskDTO]:
        results = []
        if completed is None:
            results = self.task_repo.list()

        if completed is False:
            results = self.task_repo.uncompleted_tasks()

        if completed is True:
            results = self.task_repo.completed_tasks()

        return [TaskDTO.from_entity(t) for t in results]


class CompleteTask:
    def __init__(self, task_repo: TaskRepoInterface):
        self.task_repo = task_repo

    def execute(self, task_id: str) -> TaskDTO:
        task = self.task_repo.find(id=task_id)

        if not task.completed:
            task.completed = True
            self.task_repo.update(task)
        return TaskDTO.from_entity(task)

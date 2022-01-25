from typing import List, Optional

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.param_functions import Query

from todo.containers import Container
from todo.modules.task.dtos import CreateTaskDTO, TaskDTO
from todo.modules.task.exceptions import TaskNotFoundException
from todo.modules.task.services import CompleteTask, CreateTask, ListTasks

routes = APIRouter(prefix="/tasks")


@routes.get("", response_model=List[TaskDTO])
@inject
def list_tasks(
    completed: Optional[bool] = Query(None, description="Filter tasks by their status"),
    list_tasks_service: ListTasks = Depends(Provide[Container.task.list_tasks_service]),
) -> List[TaskDTO]:
    return list_tasks_service.execute(completed)


@routes.post("", response_model=TaskDTO, status_code=status.HTTP_201_CREATED)
@inject
def create_task(
    new_task: CreateTaskDTO,
    create_task_service: CreateTask = Depends(
        Provide[Container.task.create_task_service]
    ),
) -> TaskDTO:
    return create_task_service.execute(new_task)


@routes.post("/{task_id}/complete", response_model=TaskDTO)
@inject
def complete_task(
    task_id: str,
    complete_task_service: CompleteTask = Depends(
        Provide[Container.task.complete_task_service]
    ),
) -> TaskDTO:
    try:
        return complete_task_service.execute(task_id)

    except TaskNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)

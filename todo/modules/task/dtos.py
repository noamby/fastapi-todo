from todo.modules.task.entities import BaseEntity, TaskFields


class BaseDTO:
    @classmethod
    def from_entity(cls, entity: BaseEntity):
        return cls(**{**entity.dict(), **{"id": str(entity.id)}})


class TaskDTO(TaskFields, BaseDTO):
    id: str

    class Config:
        title = "Task"


class CreateTaskDTO(TaskFields):
    class Config:
        title = "NewTask"

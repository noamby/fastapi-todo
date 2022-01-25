from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class BaseEntity(BaseModel):
    id: UUID = uuid4()

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def build(cls, **kwargs):
        return cls(**kwargs)


class TaskFields(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class Task(TaskFields, BaseEntity):
    pass

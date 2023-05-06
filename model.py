from fastapi import Form
from pydantic import BaseModel, validator
from typing import List, Optional


class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)


class TodoItem(BaseModel):
    item: str

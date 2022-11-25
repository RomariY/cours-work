import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from pydantic import Field


class OperatorSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str
    syntax: str
    example: str


class OperatorCreateSchema(BaseModel):
    name: str
    syntax: str
    example: str


class OperatorUpdateSchema(BaseModel):
    name: Optional[str]
    syntax: Optional[str]
    example: Optional[str]

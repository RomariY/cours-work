import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from pydantic import Field


class OperatorSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str = Field(None, max_length=32)
    syntax: str = Field(None, max_length=200)
    example: str


class OperatorCreateSchema(BaseModel):
    name: str = Field(None, max_length=32)
    syntax: str = Field(None, max_length=200)
    example: str


class OperatorUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=32)
    syntax: Optional[str] = Field(None, max_length=200)
    example: Optional[str]

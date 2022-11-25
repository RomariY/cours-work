import json
import uuid
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel
from pydantic import Field
from pydantic.json import pydantic_encoder


class DataTypeSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str
    description: str
    example: str


class DataTypeCreateSchema(BaseModel):
    name: str
    description: str
    example: str


class FunctionSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str
    description: str
    params: List[str]
    return_type: DataTypeSchema
    example: str
    note: str


class FunctionCreateSchema(BaseModel):
    name: str
    description: str
    params: List[str]
    return_type: UUID
    example: str
    note: str

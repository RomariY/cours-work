import json
import uuid
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel
from pydantic import Field
from pydantic.json import pydantic_encoder


class DataTypeSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str = Field(None, max_length=32)
    description: str = Field(None, max_length=200)
    example: str


class DataTypeCreateSchema(BaseModel):
    name: str = Field(None, max_length=32)
    description: str = Field(None, max_length=200)
    example: str


class FunctionSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str = Field(None, max_length=32)
    description: str = Field(None, max_length=200)
    params: List[str]
    return_type: DataTypeSchema
    example: str
    note: str = Field(None, max_length=100)


class FunctionCreateSchema(BaseModel):
    name: str = Field(None, max_length=32)
    description: str = Field(None, max_length=200)
    params: List[str]
    return_type: UUID
    example: str
    note: str = Field(None, max_length=100)


class FunctionUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=32)
    description: Optional[str] = Field(None, max_length=200)
    params: Optional[List[str]]
    return_type: Optional[UUID]
    example: Optional[str]
    note: Optional[str] = Field(None, max_length=200)

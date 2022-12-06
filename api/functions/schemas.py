import json
import uuid
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, validator
from pydantic import Field
from pydantic.json import pydantic_encoder

from api.base.models import BaseNameUnique
from api.functions.models import DataType, Function


class DataTypeSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str = Field(None, max_length=32)
    description: str = Field(None, max_length=200)
    example: str


class DataTypeCreateSchema(BaseModel, BaseNameUnique):
    name: str = Field(None, max_length=32)
    description: str = Field(None, max_length=200)
    example: str

    @validator("name")
    def name_must_be_unique(cls, value):
        return super(DataTypeCreateSchema, cls).name_must_be_unique(value, DataType)


class DataTypeUpdateSchema(BaseModel):
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


class FunctionCreateSchema(BaseModel, BaseNameUnique):
    name: str = Field(None, max_length=32)
    description: str = Field(None, max_length=200)
    params: List[str]
    return_type: UUID
    example: str
    note: str = Field(None, max_length=100)

    @validator("name")
    def name_must_be_unique(cls, value):
        return super(FunctionCreateSchema, cls).name_must_be_unique(value, DataType)


class FunctionUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=32)
    description: Optional[str] = Field(None, max_length=200)
    params: Optional[List[str]]
    return_type: Optional[UUID]
    example: Optional[str]
    note: Optional[str] = Field(None, max_length=200)

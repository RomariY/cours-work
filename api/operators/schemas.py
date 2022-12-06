import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, validator
from pydantic import Field

from api.base.models import BaseNameUnique
from api.operators.models import Operator


class OperatorSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str = Field(None, max_length=32)
    syntax: str = Field(None, max_length=200)
    example: str


class OperatorCreateSchema(BaseModel, BaseNameUnique):
    name: str = Field(None, max_length=32)
    syntax: str = Field(None, max_length=200)
    example: str

    @validator("name")
    def name_must_be_unique(cls, value):
        return super(OperatorCreateSchema, cls).name_must_be_unique(value, Operator)


class OperatorUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=32)
    syntax: Optional[str] = Field(None, max_length=200)
    example: Optional[str]

import json
import uuid
from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from pydantic import Field
from pydantic.json import pydantic_encoder


class ConstructionSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str
    description: str
    syntax: str
    example: str


class ConstructionCreateSchema(BaseModel):
    name: str = Field(None, max_length=32)
    description: str = Field(None, max_length=200)
    syntax: str
    example: str


class ConstructionUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=32)
    description: Optional[str] = Field(None, max_length=200)
    syntax: Optional[str]
    example: Optional[str]


def exclude_optional_dict(model: BaseModel):
    return {**model.dict(exclude_unset=True), **model.dict(exclude_none=True)}


def exclude_optional_json(model: BaseModel):
    return json.dumps(exclude_optional_dict(model), default=pydantic_encoder)

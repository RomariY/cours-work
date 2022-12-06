import json
import uuid
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, validator
from pydantic import Field
from pydantic.json import pydantic_encoder

from api.base.models import BaseNameUnique
from api.constructions.models import Construction


class ConstructionSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str = Field(None, max_length=32)
    description: str
    syntax: str
    example: str


class ConstructionCreateSchema(BaseModel, BaseNameUnique):
    name: str = Field(None, max_length=32)
    description: str = Field(None, max_length=200)
    syntax: str = Field(None, max_length=200)
    example: str

    @validator("name")
    def name_must_be_unique(cls, value):
        return super(ConstructionCreateSchema, cls).name_must_be_unique(value, Construction)


class ConstructionUpdateSchema(BaseModel, BaseNameUnique):
    name: Optional[str] = Field(None, max_length=32)
    description: Optional[str] = Field(None, max_length=200)
    syntax: Optional[str] = Field(None, max_length=200)
    example: Optional[str]

    @validator("name")
    def name_must_be_unique(cls, value):
        return super(ConstructionUpdateSchema, cls).name_must_be_unique(value, Construction)


def exclude_optional_dict(model: BaseModel):
    return {**model.dict(exclude_unset=True), **model.dict(exclude_none=True)}


def exclude_optional_json(model: BaseModel):
    return json.dumps(exclude_optional_dict(model), default=pydantic_encoder)

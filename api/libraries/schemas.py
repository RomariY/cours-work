import uuid
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, HttpUrl, validator
from pydantic import Field

from api.base.models import BaseNameUnique
from api.libraries.models import Library


class LibraryTypes(str, Enum):
    secure = 'Secure'
    compiling = 'Compiling'
    database = "Database"
    base = "Basic"


class LibrarySchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4())
    name: str = Field(None, max_length=50)
    type: LibraryTypes = LibraryTypes.base
    description: str = Field(None, max_length=200)
    repo_link: HttpUrl


class LibraryCreateSchema(BaseModel, BaseNameUnique):
    name: str = Field(None, max_length=50)
    type: LibraryTypes = LibraryTypes.base
    description: str = Field(None, max_length=200)
    repo_link: HttpUrl

    @validator("name")
    def name_must_be_unique(cls, value):
        return super(LibraryCreateSchema, cls).name_must_be_unique(value, Library)

    @validator("repo_link")
    def validate_repo_link(cls, value):
        model = Library
        filter_dict = {"repo_link": value}
        if model.get_or_none(**filter_dict):
            raise ValueError(f"{model.__name__} with name {value} already exists")
        return value


class LibraryUpdateSchema(BaseModel, BaseNameUnique):
    name: Optional[str] = Field(None, max_length=50)
    type: Optional[LibraryTypes] = LibraryTypes.base
    description: Optional[str] = Field(None, max_length=200)
    repo_link: Optional[HttpUrl]

    @validator("name")
    def name_must_be_unique(cls, value):
        return super(LibraryUpdateSchema, cls).name_must_be_unique(value, Library)

    @validator("repo_link")
    def validate_repo_link(cls, value):
        model = Library
        filter_dict = {"repo_link": value}
        if model.get_or_none(**filter_dict):
            raise ValueError(f"{model.__name__} with name {value} already exists")
        return value

import uuid
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, HttpUrl
from pydantic import Field


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


class LibraryCreateSchema(BaseModel):
    name: str = Field(None, max_length=50)
    type: LibraryTypes = LibraryTypes.base
    description: str = Field(None, max_length=200)
    repo_link: HttpUrl


class LibraryUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    type: Optional[LibraryTypes] = LibraryTypes.base
    description: Optional[str] = Field(None, max_length=200)
    repo_link: Optional[HttpUrl]

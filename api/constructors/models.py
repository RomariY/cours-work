import peewee
from playhouse.postgres_ext import ArrayField

from api.base.models import BaseModel, UUIDModel


class Construction(UUIDModel):
    name = peewee.CharField(max_length=32)
    description = peewee.CharField(max_length=200)
    syntax = peewee.CharField(max_length=200)
    example = peewee.TextField()



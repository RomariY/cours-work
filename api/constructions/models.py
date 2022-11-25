import peewee

from api.base import database
from api.base.models import PeeweeGetterDict
from api.base.models import UUIDModel


class Construction(UUIDModel):
    name = peewee.CharField(max_length=32)
    description = peewee.CharField(max_length=200)
    syntax = peewee.CharField(max_length=200)
    example = peewee.TextField()

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


database.psql.create_tables([Construction])

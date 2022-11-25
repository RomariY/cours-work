import peewee
import playhouse.postgres_ext as pg

from api.base import database
from api.base.models import PeeweeGetterDict
from api.base.models import UUIDModel


class DataType(UUIDModel):
    name = peewee.CharField(max_length=32)
    description = peewee.CharField(max_length=200)
    example = peewee.TextField()

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class Function(UUIDModel):
    name = peewee.CharField(max_length=32)
    description = peewee.CharField(max_length=200)
    params = pg.ArrayField(pg.CharField, default=[])
    return_type = peewee.ForeignKeyField(DataType, backref="data_types")
    example = peewee.TextField()
    note = peewee.CharField(max_length=100)

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


database.psql.create_tables([DataType, Function])

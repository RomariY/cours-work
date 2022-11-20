import peewee
from playhouse.postgres_ext import ArrayField

from api.base.models import UUIDModel


class DataType(UUIDModel):
    name = peewee.CharField(max_length=32)
    description = peewee.CharField(max_length=200)
    example = peewee.TextField()


class Function(UUIDModel):
    name = peewee.CharField(max_length=32)
    description = peewee.CharField(max_length=200)
    params = ArrayField(peewee.CharField(max_length=16))
    return_type = peewee.ForeignKeyField(DataType, backref="data_types")
    example = peewee.TextField()
    note = peewee.CharField(max_length=100)




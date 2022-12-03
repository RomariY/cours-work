import datetime
import uuid
from typing import Any

import peewee
from pydantic.utils import GetterDict

from api.base.database import psql


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class UUIDModel(peewee.Model):
    """Parent for all app's models"""
    id = peewee.TextField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True
        database = psql


class BaseModel(peewee.Model):
    """Parent for all app's models"""
    id = peewee.TextField(primary_key=True, default=uuid.uuid4)
    created = peewee.DateTimeField(default=datetime.datetime.now)
    modified = peewee.DateTimeField()

    def save(self, *args, **kwargs):
        self.modified = datetime.datetime.now()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
        database = psql


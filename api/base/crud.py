from uuid import UUID
from playhouse.shortcuts import model_to_dict

from api.base.database import psql


class CrudBase(object):
    def __init__(self, cls):
        self.cls = cls

    def get_obj(self, pk: UUID):
        return self.cls.filter(self.cls.id == pk).first()

    def get_objs(self, skip: int = 0, limit: int = 100) -> object:
        return list(self.cls.select().offset(skip).limit(limit).dicts())

    def create_obj(self, **kwargs):
        obj = None
        with psql.atomic() as transaction:
            try:
                obj = self.cls.create(**kwargs)
                obj = model_to_dict(obj)
            except Exception:
                transaction.rollback()
                error_saving = True
                raise Exception(f"The database failed in creation an object for model {self.cls}")

        return obj

    def delete_obj(self, pk: UUID):
        self.cls.delete().where(self.cls.id == pk).execute()

from uuid import UUID
from playhouse.shortcuts import model_to_dict


class CrudBase(object):
    def __init__(self, cls):
        self.cls = cls

    def get_obj(self, pk: UUID):
        return self.cls.filter(self.cls.id == pk).first()

    def get_objs(self, skip: int = 0, limit: int = 100) -> object:
        return list(self.cls.select().offset(skip).limit(limit).dicts())

    def create_obj(self, **kwargs):
        obj = self.cls.create(**kwargs)
        return model_to_dict(obj)

    def delete_obj(self, pk: UUID):
        self.cls.delete().where(self.cls.id == pk).execute()

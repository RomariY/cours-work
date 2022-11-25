import logging
from uuid import UUID

import peewee

logger = logging.getLogger()


def serialize_dict(value: dict):
    for key in value.keys():
        value[key] = str(value[key])
    return value


def check_pk_exist(model, pk: UUID):
    try:
        exist_status = model.select().where(model.id == pk).exists()
    except ValueError:
        raise ValueError("Check your model")
    return exist_status

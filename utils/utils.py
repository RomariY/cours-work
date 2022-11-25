import logging

logger = logging.getLogger()


def serialize_dict(value: dict):
    for key in value.keys():
        value[key] = str(value[key])
    return value

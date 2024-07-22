from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import registry
import datetime


def serialize(obj):
    if isinstance(obj, list):
        result = []
        for i in range(0, len(obj)):
            result.append(serialize_func(obj[i]))
        return result
    else:
        return serialize_func(obj)


def serialize_func(obj):
    # Сериализация объекта
    _visited_objs = []
    if isinstance(obj.__class__, DeclarativeMeta):
        if obj in _visited_objs:
            return None
        _visited_objs.append(obj)

        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            if isinstance(obj.__getattribute__(field), datetime.datetime):
                fields[field] = obj.__getattribute__(field).strftime('%d.%m.%Y')
            elif isinstance(obj.__getattribute__(field), datetime.date):
                fields[field] = obj.__getattribute__(field).strftime('%d.%m.%Y')
            elif isinstance(obj.__getattribute__(field), registry):
                pass
            elif isinstance(obj.__getattribute__(field).__class__, DeclarativeMeta):
                fields[field] = serialize_func(obj.__getattribute__(field))
            else:
                fields[field] = obj.__getattribute__(field)

        return fields

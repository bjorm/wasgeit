import datetime
from flask import json


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, datetime.date):
                return obj.isoformat()

            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)

        return json.JSONEncoder.default(self, obj)

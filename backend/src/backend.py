import datetime
from flask import Flask, json
from flask.json import JSONEncoder
from wasgeit import Agenda


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, datetime.date):
                return obj.isoformat()

            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

agenda = Agenda()

@app.route("/rest/agenda")
def hello():
    return json.dumps(agenda.get())

if __name__ == "__main__":
    app.run(debug=True)
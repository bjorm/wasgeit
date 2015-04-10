import datetime
from flask import Flask, json, request
from agenda import Agenda


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


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

agenda = Agenda()

@app.route("/rest/agenda")
def hello():
    venue_ids_str = request.args.get('venues', '')
    venue_ids = set() if len(venue_ids_str) == 0 else {int(id_str) for id_str in venue_ids_str.split(',')}

    return json.dumps(agenda.get(venue_ids))

if __name__ == "__main__":
    app.run(debug=True)
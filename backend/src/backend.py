from flask import Flask, request, json, Blueprint
from agenda import Agenda
from util import CustomJSONEncoder
import logging

rest = Blueprint('rest', __name__, url_prefix="")


@rest.route("/agenda")
def get_agenda():
    venue_ids_str = request.args.get('venues', '')
    venue_ids = set() if len(venue_ids_str) == 0 else {int(id_str) for id_str in venue_ids_str.split(',')}

    return json.dumps(agenda.get_events(venue_ids))


@rest.route("/venues")
def get_venues():
    return json.dumps(agenda.get_venues())

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
app.register_blueprint(rest)

agenda = Agenda()

if __name__ == "__main__":
    app.run(debug=True)

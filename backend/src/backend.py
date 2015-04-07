from flask import Flask, json
from wasgeit import Agenda

app = Flask(__name__)

agenda = Agenda()

@app.route("/rest/agenda")
def hello():
    return json.jsonify(agenda.get())

if __name__ == "__main__":
    app.run(debug=True)
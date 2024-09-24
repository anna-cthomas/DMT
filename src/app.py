import flask

app = flask.Flask(__name__)

@app.route('/', defaults={'path': 'index.html'})
@app.route("/<path:path>")
def index(path):
    return flask.send_from_directory("../static", path)

@app.route("/api/test")
def test():
    return "BYE"

app.run(host="0.0.0.0", port=1024, debug=True)
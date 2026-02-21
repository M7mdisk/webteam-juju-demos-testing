import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Hello from yet another Juju Demo! 🚀"


if __name__ == "__main__":
    app.run()

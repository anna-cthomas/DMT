import flask
import twscrape
import os
import dotenv

app = flask.Flask(__name__)

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
dotenv.load_dotenv(dotenv_path)
dotenv.load_dotenv(dotenv.find_dotenv(usecwd=True), override=True)

users = os.environ.get("USERS")
users_pass = os.environ.get("USERS_PASS")
emails = os.environ.get("EMAILS")
emails_pass = os.environ.get("EMAILS_PASS")


@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def index(path):
    return flask.send_from_directory("../static", path)


@app.route("/api/test")
async def test():
    print(users, users_pass, emails, emails_pass)
    api = twscrape.API()  # or API("path-to.db") - default is `accounts.db`

    # Add accounts, login
    await api.pool.login_all()

    # Testing search & scrape to see if logged in accounts are working
    test_return = str(await twscrape.gather(api.search("elon musk", limit=20)))

    return test_return


app.run(host="0.0.0.0", port=1024, debug=True)
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
    # test_search_default = str(await twscrape.gather(api.search("elon musk", limit=20)))

    # tweet info
    # For testing:
    # A tweet with no replies (mitsuri art, replies are disabled)
    # tweet_id = 1838261747624612135
    # A tweet with replies (weed pikachu)
    tweet_id = 1838560744738095403

    # test_tweet_retrieval = await api.tweet_details(tweet_id)  # Works
    # test_tweet_retweets = await twscrape.gather(api.retweeters(tweet_id, limit=20)) # Works

    # Note: this method have small pagination from X side, like 5 tweets per query
    # test_tweet_replies = await twscrape.gather(api.tweet_replies(tweet_id, limit=20))  # Works

    return str(tweet_id)


app.run(host="0.0.0.0", port=1024, debug=True)
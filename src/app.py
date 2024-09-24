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

    # ADD ACCOUNTS (for CLI usage see BELOW)
    # Split the user into the twitter username, twitter password, twitter email, twitter email password
    # users_info = users.split(",")

    # or add account with COOKIES (with cookies login not required)
    cookies =   """"""

    await api.pool.add_account("gilgameshxone", "", "", "", cookies=cookies)
    await api.pool.login_all()
    # tweet info
    tweet_id = 20
    test_return = str(await api.tweet_details(tweet_id))  # Tweet
    # await twscrape.gather(api.retweeters(tweet_id, limit=20))  # list[User]

    # # get user by login
    # user_login = "xdevelopers"
    # await api.user_by_login(user_login)  # User

    # # user info
    # user_id = 2244994945
    # await api.user_by_id(user_id)  # User
    # await twscrape.gather(api.following(user_id, limit=20))  # list[User]
    # await twscrape.gather(api.followers(user_id, limit=20))  # list[User]
    # await twscrape.gather(api.verified_followers(user_id, limit=20))  # list[User]
    # await twscrape.gather(api.subscriptions(user_id, limit=20))  # list[User]
    # await twscrape.gather(api.user_tweets(user_id, limit=20))  # list[Tweet]
    # await twscrape.gather(api.user_tweets_and_replies(user_id, limit=20))  # list[Tweet]

    # # list info
    # list_id = 123456789
    # await twscrape.gather(api.list_timeline(list_id))

    # # NOTE 1: gather is a helper function to receive all data as list, FOR can be used as well:
    # async for tweet in api.search("elon musk"):
    #     print(
    #         tweet.id, tweet.user.username, tweet.rawContent
    #     )  # tweet is `Tweet` object

    # # NOTE 2: all methods have `raw` version (returns `httpx.Response` object):
    # async for rep in api.search_raw("elon musk"):
    #     print(rep.status_code, rep.json())  # rep is `httpx.Response` object

    # # change log level, default info
    # twscrape.set_log_level("DEBUG")

    # # Tweet & User model can be converted to regular dict or json, e.g.:
    # doc = await api.user_by_id(user_id)  # User
    # doc.dict()  # -> python dict
    # doc.json()  # -> json string

    return test_return


app.run(host="0.0.0.0", port=1024, debug=True)
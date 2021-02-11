import praw
from datetime import datetime
import textwrite

r = praw.Reddit(
    client_id="bvnDzvUpzBhnhw",
    client_secret="1n7gUFkbdqa8cBR4HkoLoDDzRPU80g",
    user_agent="Reddit Test by /u/bazko",
    username="bazko",
    password="macoprcosc1"
)

for comment in r.subreddit('Bitcoin').stream.comments():
    textwrite.textwrite()

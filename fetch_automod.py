import praw
import os

def fetch_automod_config():
    reddit = praw.Reddit(
        client_id=os.environ['REDDIT_CLIENT_ID'],
        client_secret=os.environ['REDDIT_SECRET'],
        username=os.environ['REDDIT_USERNAME'],
        password=os.environ['REDDIT_PASSWORD'],
        user_agent='test'
    )

    subreddit = reddit.subreddit('test') # Your subreddit name
    automod_config = subreddit.wiki['config/automoderator'].content_md

    with open('automod/automoderator.yml', 'w') as file:
        file.write(automod_config)

if __name__ == '__main__':
    fetch_automod_config()

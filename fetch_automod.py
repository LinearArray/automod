import praw
import os

def fetch_automod_config():
    reddit = praw.Reddit(
        client_id=os.environ['REDDIT_CLIENT_ID'],
        client_secret=os.environ['REDDIT_SECRET'],
        username=os.environ['REDDIT_USERNAME'],
        password=os.environ['REDDIT_PASSWORD'],
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    )

    subreddit = reddit.subreddit(os.environ['SUBREDDIT_NAME'])  
    automod_config = subreddit.wiki['config/automoderator'].content_md

    with open('automod/automoderator.yml', 'w') as file:
        file.write(automod_config)

if __name__ == '__main__':
    fetch_automod_config()

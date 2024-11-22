import praw
import os

def update_automod_config():
    reddit = praw.Reddit(
        client_id=os.environ['REDDIT_CLIENT_ID'],
        client_secret=os.environ['REDDIT_SECRET'],
        username=os.environ['REDDIT_USERNAME'],
        password=os.environ['REDDIT_PASSWORD'],
        user_agent='test'
    )

    subreddit = reddit.subreddit('test') # replace with your subreddit name

    with open('automod/automoderator.yml', 'r') as file:
        automod_config = file.read()

    committer = os.environ['GITHUB_ACTOR']
    commit_id = os.environ['GITHUB_SHA']
    commit_reason = f"Changes by {committer} on {commit_id}"

    subreddit.wiki['config/automoderator'].edit(automod_config, reason=commit_reason)

if __name__ == '__main__':
    update_automod_config()

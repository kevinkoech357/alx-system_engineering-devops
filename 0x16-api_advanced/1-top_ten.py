#!/usr/bin/python3

"""
Queries the REDDIT API.
"""


import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit

    Args:
        subreddit: The name of the subreddit to query.
    """

    # Set a custom User-Agent to avoid errors related to Too Many Requests.
    headers = {"User-Agent": "Karma/0.1"}

    # Make a request to the Reddit API to get the subreddit's information.
    response = requests.get(
            f"https://api.reddit.com/r/{subreddit}/hot.json?limit=10",
            headers=headers)

    if response.status_code == 200:
        # Get the subreddit's hot posts from the response.
        hot_posts = response.json()["data"]["children"]
        # Print the titles of the first 10 hot posts.
        for post in hot_posts[:10]:
            print(post["data"]["title"])
    else:
        print('None')

#!/usr/bin/python3

"""
Query REDDIT API.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit: The name of the subreddit to query.
        hot_list: A list to store the titles of the hot articles.
    """
    # Set a custom User-Agent to avoid errors related to Too Many Requests.
    headers = {"User-Agent": "Karma/0.1"}

    # Make a request to the Reddit API to get the subreddit's hot posts.
    response = requests.get(
            f"https://api.reddit.com/r/{subreddit}/hot.json?limit=100",
            headers=headers, allow_redirects=False)

    if response.status_code == 200:
        # Get the subreddit's hot posts from the response.
        hot_posts = response.json()["data"]["children"]
        # Extract the titles of the hot posts.
        for post in hot_posts:
            hot_list.append(post["data"]["title"])
        # Check if there are more pages of results.
        if "after" in response.json()["data"]:
            # Recursively query the next page of results.
            return recurse(subreddit, hot_list=hot_list)
        else:
            # All pages of results have been queried.
            return hot_list
    else:
        return None

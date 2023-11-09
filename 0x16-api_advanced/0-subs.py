#!/usr/bin/python3

"""
Queries the REDDIT API.
"""


import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit: The name of the subreddit to query.

    Returns:
        The number of subscribers for the given subreddit,
        or 0 if the subreddit is invalid.
    """

    # Set a custom User-Agent to avoid errors related to Too Many Requests.
    headers = {"User-Agent": "Karma/0.1"}

    # Make a request to the Reddit API to get the subreddit's information.
    response = requests.get(f"https://api.reddit.com/r/{subreddit}/about.json",
                            headers=headers)

    if response.status_code == 200:
        subreddit_info = response.json()
        return (subreddit_info['data']['subscribers'])
    return 0

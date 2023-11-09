#!/usr/bin/python3

"""
Query REDDIT API
"""

from collections import Counter
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.
    """
    # Set a custom User-Agent to avoid errors related to Too Many Requests.
    headers = {"User-Agent": "Karma/0.1"}

    # Initialize counts if not provided.
    if counts is None:
        counts = Counter()

    # Make a request to the Reddit API to get the subreddit's hot posts.
    response = requests.get(
        "https://api.reddit.com/r/{}/hot.json?limit=100&after={}"
        .format(subreddit, after),
        headers=headers, allow_redirects=False)

    if response.status_code == 200:
        # Get the subreddit's hot posts from the response.
        hot_posts = response.json().get("data", {}).get("children", [])

        # Extract the titles of the hot posts.
        for post in hot_posts:
            title = post["data"]["title"].lower()

            # Check if the title contains any of the keywords.
            for word in word_list:
                # Check for whole word match (not part of a larger word).
                if f' {word} ' in f' {title} ':
                    counts[word] += 1

        # Check if there are more pages of results.
        next_page_after = response.json().get("data", {}).get("after")
        if next_page_after:
            # Recursively query the next page of results.
            count_words(subreddit, word_list, after=next_page_after,
                        counts=counts)
        else:
            for keyword, count in sorted(counts.items(),
                                         key=lambda x: (-x[1], x[0])):
                print(f"{keyword}: {count}")
    else:
        # Print nothing for unsuccessful requests.
        return None

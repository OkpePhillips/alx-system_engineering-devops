#!/usr/bin/python3
"""
A script that returns the number of subscribers of a subreddit
using the reddit api.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ Queries to Reddit API """

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "AdvancedApi"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data['data']['subscribers']

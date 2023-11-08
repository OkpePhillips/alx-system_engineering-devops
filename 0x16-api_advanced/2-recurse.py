#!/usr/bin/python3
"""
Recursively calling an api endpoint and printing result using requests.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    if subreddit is None:
        return None

    params = {
            'after': after
            }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'api_advanced'}
    response = requests.get(url, params=params,
                            headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

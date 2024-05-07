#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code != 200:
        print('None')
        return

    try:
        posts = response.json()['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    except KeyError:
        print("None")

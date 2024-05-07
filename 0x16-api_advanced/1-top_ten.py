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
    response_json = response.json()

    try:
        posts = response_json['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    except Exception:
        print("None")

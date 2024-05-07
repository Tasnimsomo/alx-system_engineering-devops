#!/usr/bin/python3

""" Top Ten """
import requests


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, allow_redirects=False)
    if response.status_code != 200:
        print('None')
        return
    response_json = response.json()

    if 'data' not in response_json or 'children' not in response_json['data']:
        print('None')
        return
    posts = response_json['data']['children']
    for post in posts:
        title = post['data']['title']
        print(title)

#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code != 200:
            print('None')
            return
    
        posts = response.json()['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    except Exception:
        print("None")

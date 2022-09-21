#!/usr/bin/python3
"""
1. Top Ten
"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10 hot posts listed
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        posts = data['data']['children']
        for post in posts[:10]:
            print(post['data']['title'])
    else:
        print(None)

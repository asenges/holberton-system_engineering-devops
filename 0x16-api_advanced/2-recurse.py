#!/usr/bin/python3
"""
2. Recurse it!
"""
import requests
import sys


def recurse(subreddit, hot_list=[]):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if data['data']['after']:
            print(post['data']['title'])
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None

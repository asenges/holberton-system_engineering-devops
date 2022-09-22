#!/usr/bin/python3
"""
2. Recurse it!
"""
import pprint
import requests
import sys


def recurse(subreddit, hot_list=[]):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/105.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        i = 0
        for post in data['data']['children']:
            i += 1
            #print(i, post['data']['title'])
            hot_list.append(post['data']['title'])
        if data['data']['after']:#!= 't3_xkgyiq':
            #print("Data After", data['data']['after'])
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None

#!/usr/bin/python3
"""
================================================================================
function that queries the Reddit API and prints the titles of the first 10 hot
 posts listed for a given subreddit.
================================================================================
"""

import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agent': 'custom agent'}
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code == 200:
        for i in r.json().get('data').get('children'):
            print(i.get('data').get('title'))
    else:
        print(None)

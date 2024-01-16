#!/usr/bin/python3
"""
================================================================================
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
 subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests, ensure you’re setting a
 custom User-Agent.
================================================================================
"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'custom agent'}
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code == 200:
        return(r.json().get('data').get('subscribers'))
    else:
        return 0

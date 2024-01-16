#!/usr/bin/python3
"""
================================================================================
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.
Hint: The Reddit API uses pagination for separating pages of responses.
Requirements:
   Prototype: def recurse(subreddit, hot_list=[])
   Note: You may change the prototype, but it must be able to be called with
   just a subreddit supplied. AKA you can add a counter, but it must work
   without supplying a starting value in the main.
   If not a valid subreddit, return None.
   NOTE: Invalid subreddits may return a redirect to search results. Ensure
   that you are not following redirects.
================================================================================
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    function that return recursively all titles of all hot articles
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    header = {'User-Agent': 'custom agent'}
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code == 200:
        for i in range(r.json().get('data').get('dist')):
            hot_list.append('x')
            a = r.json().get('data').get('after')
        if (a):
            return (recurse(subreddit, hot_list, a))
        else:
            return hot_list
    else:
        return None

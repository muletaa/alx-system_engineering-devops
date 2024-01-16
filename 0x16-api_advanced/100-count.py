#!/usr/bin/python3
"""
================================================================================
recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
Javascript should count as javascript, but java should not)
================================================================================
"""

import requests


def count_words(subreddit, word_list):
    """
    recursive function that queries the Reddit API, parses the title of all hot
    articles, and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    header = {'User-Agent': 'custom agent'}
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code == 200:
        a = r.json().get('data').get('after')
        if (a):
            return (recurse(subreddit, hot_list, a))
        else:
            return hot_list
    else:
        return None

#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should
return 0.
"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        return 0
    else:
        return 0

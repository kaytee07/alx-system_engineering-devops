#!/bin/usr/python3
"""
function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        lists = data['data']['children']

        for data in lists:
            print(data['data']['title'])
    else:
        print(None)

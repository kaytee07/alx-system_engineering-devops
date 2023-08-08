#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If
no results are found for the given subreddit, the function should
return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else None

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']

        if not articles:
            return hot_list

        for article in articles:
            hot_list.append(article['data']['title'])

        next_after = data['data']['after']
        if next_after:
            return recurse(subreddit, hot_list, next_after)
        else:
            return hot_list
    elif response.status_code == 404:
        return None

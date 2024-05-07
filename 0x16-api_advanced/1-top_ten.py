#!/usr/bin/python3
"""Queries and print title of 1st 10 posts"""
import requests


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}

    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get("data")
        [print(i.get("data").get("title")) for g in posts.get("children")]
    print("None")
    return

#!/usr/bin/python3
"""Queries subreddit's subscribers"""
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    mySubscribers = response.json().get("data")
    return mySubscribers.get("subscribers")

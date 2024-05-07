#!/usr/bin/python3
"""Queries subreddit's subscribers"""
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        mydata = response.json()
        mySubscribers = mydata['data']['subscribers']
        return mySubscribers
    else:
        print("Error:", response.status_code)
        return 0

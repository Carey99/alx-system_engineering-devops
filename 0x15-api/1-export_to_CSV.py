#!/usr/bin/python3
"""Exporting script to CSV"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = f'{url}/users/{sys.argv[1]}'
    todo_url = f'{url}/todos?userId={sys.argv[1]}'

    user_data = requests.get(user).json()
    todos_data = requests.get(todo_url).json()

    name = user_data["username"]
    user_id = sys.argv[1]

    with open("{}.csv".format(user_id), mode="w") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos_data:
            csv_writer.writerow([todo['userId'],
                                name,
                                todo['completed'],
                                todo['title']])

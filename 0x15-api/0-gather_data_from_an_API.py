#!/usr/bin/python3
"""Gathering todo list of user"""
import requests
import sys


def todo_list(emp_id):
    url = "https://jsonplaceholder.typicode.com"
    user_url = f'{url}/users/{emp_id}'
    todo_url = f'{url}/todos?userId={emp_id}'

    emp_data = requests.get(user_url).json()
    name = emp_data["name"]

    todo_data = requests.get(todo_url).json()
    total = len(todo_data)

    completed = 0
    for todo in todo_data:
        if todo["completed"] is True:
            completed += 1
    print("Employee {} is done with tasks({}/{}):".format(
        name, completed, total))

    for todo in todo_data:
        if todo["completed"] is True:
            print(f'\t {todo["title"]}')


if __name__ == "__main__":
    todo_list(int(sys.argv[1]))

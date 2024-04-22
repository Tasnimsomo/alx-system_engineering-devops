#!/usr/bin/python3
"""extend your Python script to export data in the JSON format."""

import json
import requests
import sys


if __name__ == "__main__":
    users_res = requests.get('https://jsonplaceholder.typicode.com/users')
    todos_res = requests.get('https://jsonplaceholder.typicode.com/todos')

    users = users_res.json()
    todos = todos_res.json()

    user_tasks = {}
    for user in users:
        user_todos = [todo for todo in todos if todo.get(
            'userId') == user.get('id')]
        tasks = []
        for todo in user_todos:
            task = {
                "username": user.get('username'),
                "task": todo.get('title'),
                "completed": todo.get('completed')}
            tasks.append(task)
        user_tasks[user.get('id')] = tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file)

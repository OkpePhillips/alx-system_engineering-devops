#!/usr/bin/python3
"""
Module to access an api endpoint using requests
and create a json dictionary of list file from the data
"""
import json
import requests
import sys

if __name__ == '__main__':
    users_url = f'https://jsonplaceholder.typicode.com/users'
    todo_url = f'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(users_url).json()
    todo = requests.get(todo_url).json()
    task_file = {}
    for user in users:
        user_task = []
        for task in todo:
            if user['id'] == task['userId']:
                task_info = {'username': user['username'],
                             'task': task['title'],
                             'completed': task['completed']}
                user_task.append(task_info)
        task_file[user['id']] = user_task
    with open('todo_all_employees.json', 'w') as file:
        json.dump(task_file, file)

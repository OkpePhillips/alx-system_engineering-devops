#!/usr/bin/python3
"""
Module to access an api endpoint using requests
and create a csv file from the data
"""
import json
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/todos?'\
               f'userId={employee_id}'
    employee = requests.get(user_url).json()
    employee_name = employee.get("username")
    todo = requests.get(todo_url).json()
    task_data = []
    for task in todo:
        task_info = {'task': task['title'],
            'completed': task['completed'],
            'username': employee_name}
        task_data.append(task_info)
    task_file = {employee_id: task_data}
    with open('{}.json'.format(employee_id), 'w') as file:
        json.dump(task_file, file)

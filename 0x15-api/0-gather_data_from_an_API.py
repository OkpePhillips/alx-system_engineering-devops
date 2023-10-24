#!/usr/bin/python3
"""
Module to access an api endpoint using requests
and print the data retrieved in nicely formatted way
"""
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/todos?'\
               f'userId={employee_id}'
    employee = requests.get(user_url).json()
    employee_name = employee.get("name")
    todo = requests.get(todo_url).json()
    completed = 0
    total = 0
    completed_task = []
    for id in todo:
        if id['completed']:
            completed += 1
            completed_task.append(id['title'])
        total += 1
    print("Employee {} is done with tasks({}/{})".format(
          employee_name, completed, total))
    for task in completed_task:
        print('\t {}'.format(task))

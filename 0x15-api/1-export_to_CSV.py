#!/usr/bin/python3
"""
Module to access an api endpoint using requests
and create a csv file from the data
"""
import csv
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
    tasks = []
    with open('{}.csv'.format(employee_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow(
                           [str(task['userId']),
                            f'{employee_name}',
                            str(task['completed']),
                            f'{task["title"]}'
                            ])

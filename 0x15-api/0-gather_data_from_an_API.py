#!/usr/bin/python3
"""
Module to access an api endpoint and print the output.
"""
if __name__ == '__main__':
    import requests
    import sys


    def access_api(employee_id):
        """
        Method to fetch todo list information of an
        employee.
        """
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
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

access_api(sys.argv[1])

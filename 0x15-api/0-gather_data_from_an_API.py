#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""
import json
import urllib.request
import sys


def get_data(employee_id):
    url = 'https://jsonplaceholder.typicode.com/'
    todos = url + 'todos'
    users = url + f'users/{employee_id}'
    num_of_task = 0
    num_of_comp_task = 0
    employee_name = ''
    comp_task = []

    try:
        with urllib.request.urlopen(todos) as response:
            raw_data = response.read()
            info = json.loads(raw_data)
            for todos in info:
                if todos['userId'] == int(employee_id):
                    num_of_task += 1
                    if todos['completed'] is True:
                        num_of_comp_task += 1
                        comp_task.append(todos['title'])

        with urllib.request.urlopen(users) as response:
            raw_data = response.read()
            info = json.loads(raw_data)
            employee_name = info['name']
        print('Employee {} is done with tasks({}/{}):'.
              format(employee_name, num_of_comp_task, num_of_task))
        for task in comp_task:
            print(f'\t{task}')

    except urllib.error.HTTPError as e:
        print(f'Error: {e.code}, {e.reason}')
    except urllib.error.URLError as e:
        print(f'Error: {e.reason}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("pass the the employee id")
    else:
        get_data(sys.argv[1])

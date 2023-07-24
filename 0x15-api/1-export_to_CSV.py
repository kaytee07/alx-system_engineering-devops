#!/usr/bin/python3
"""
write to csv
"""
import csv
import requests
import sys


def get_data(employee_id):
    url = 'https://jsonplaceholder.typicode.com/'
    todos_endpoint = f'todos?userId={employee_id}'
    user_endpoint = f'users/{employee_id}'
    comp_task = []

    try:
        todos_response = requests.get(url + todos_endpoint)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        user_response = requests.get(url + user_endpoint)
        user_response.raise_for_status()
        user_data = user_response.json()
        username = user_data['username']

        for todo in todos_data:
            if todo['completed']:
                comp_task.append(todo['title'])

        with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
            fieldnames = ['Employee ID', 'Username', 'Completed', 'Task']
            csv_writer = csv.DictWriter(csvfile,
                                        fieldnames=fieldnames,
                                        quoting=csv.QUOTE_ALL)
            csv_writer.writeheader()
            for task in comp_task:
                csv_writer.writerow({'Employee ID':
                                     employee_id, 'Username':
                                     username, 'Completed': 'True', 'Task':
                                     task})
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Pass the employee id as an argument.")
    else:
        get_data(sys.argv[1])

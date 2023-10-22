#!/usr/bin/python3

"""
This file contains a function that calls a fake
api and displays dummy data.
"""

# Importing libraries
import requests
import json
import sys


def get_employee_todo_progress(employee_id):
    # Define the API endpoint with the employee_id
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Send a GET request to the API
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Unable to fetch data for employee {employee_id}")
        return

    todos = response.json()

    # Get the employee name
    employee_name = todos[0]['userId']

    # Calculate the number of completed tasks and total tasks
    completed_tasks = [task for task in todos if task['completed']]
    completed = len(completed_tasks)
    total_tasks = len(todos)

    print("Employee {} is done with tasks {}/{}: "
          .format(employee_name, completed, total_tasks))

    # Print the titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        try:
            # Get the employee ID from the command-line argument
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please enter a valid employee ID (an integer).")

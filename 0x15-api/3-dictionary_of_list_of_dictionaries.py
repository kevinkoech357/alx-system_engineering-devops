#!/usr/bin/python3

"""
This file contains a function that calls a fake
API and displays dummy data.
"""

# Importing libraries
import requests
import json
import sys
import os


def fetch_employee_name(employee_id):
    # Define the API endpoint to fetch the employee name
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    # Send a GET request to the API to fetch the user information
    response = requests.get(user_url)

    if response.status_code != 200:
        return None

    user_data = response.json()
    return user_data.get('name', f'Employee {employee_id}')


def get_all_employee_todo_data():
    all_employee_data = {}  # Dictionary to store data for all employees

    for employee_id in range(1, 11):
        # Get the employee name
        employee_name = fetch_employee_name(employee_id)

        if employee_name is not None:
            # Define the API endpoint with the employee_id
            url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                    employee_id)

            # Send a GET request to the API
            response = requests.get(url)

            if response.status_code == 200:
                todos = response.json()

                # Create a list for the employee's tasks
                employee_tasks = []
                for task in todos:
                    employee_tasks.append({
                        "username": employee_name,
                        "task": task['title'],
                        "completed": task['completed']
                    })

                all_employee_data[employee_id] = employee_tasks

    return all_employee_data


def create_json_file(filename, data):
    """Creates a JSON file if it doesn't exist.

    Args:
        filename: The name of the JSON file.
        data: The data to be written to the JSON file.
    """

    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)


if __name__ == "__main__":
    json_filename = 'todo_all_employees.json'
    all_employee_data = get_all_employee_todo_data()

    create_json_file(json_filename, all_employee_data)

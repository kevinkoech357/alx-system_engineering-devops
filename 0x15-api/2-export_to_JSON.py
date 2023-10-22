#!/usr/bin/python3

"""
This file contains a function that calls a fake
API and displays dummy data.
"""

# Importing libraries
import requests
import json
import sys
import csv


def fetch_employee_name(employee_id):
    # Define the API endpoint to fetch the employee name
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    # Send a GET request to the API to fetch the user information
    response = requests.get(user_url)

    if response.status_code != 200:
        return None

    user_data = response.json()
    return user_data.get('name', f'Employee {employee_id}')


def export_to_json(employee_id, employee_name, todos):
    json_filename = f'{employee_id}.json'
    json_data = {
        employee_id: [{"task": task['title'], "completed": task['completed'],
                       "username": employee_name} for task in todos]
    }

    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file)


def get_employee_todo_progress(employee_id):
    # Get the employee name
    employee_name = fetch_employee_name(employee_id)

    if employee_name is None:
        print(f"Error: Unable to fetch data for employee {employee_id}")
        return

    # Define the API endpoint with the employee_id
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Send a GET request to the API
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Unable to fetch TODO data for employee {employee_id}")
        return

    todos = response.json()

    # Export total tasks to CSV
    export_to_json(employee_id, employee_name, todos)


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

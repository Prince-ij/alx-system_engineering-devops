#!/usr/bin/env python3
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200 or todo_response.status_code != 200:
        print("Failed to fetch data from the API")
        return

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data["name"]
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task["completed"]]
    num_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks
         ({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

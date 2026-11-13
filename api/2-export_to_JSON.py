#!/usr/bin/python3
"""Export an employee's TODO list data to JSON format."""
import json
import sys
import urllib.request


def export_to_JSON(user_id):
    """Export all tasks owned by the employee to a JSON file."""
    base = "https://jsonplaceholder.typicode.com"
    user_resp = urllib.request.urlopen(
        "{}/users/{}".format(base, user_id))
    user = json.loads(user_resp.read().decode("utf-8"))

    todos_resp = urllib.request.urlopen(
        "{}/todos?userId={}".format(base, user_id))
    todos = json.loads(todos_resp.read().decode("utf-8"))

    username = user.get("username")
    data = {user_id: []}
    for task in todos:
        data[user_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    with open("{}.json".format(user_id), "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    export_to_JSON(sys.argv[1])

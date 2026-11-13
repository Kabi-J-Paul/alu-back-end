#!/usr/bin/python3
"""Export all employees' TODO list data to JSON format."""
import collections
import json
import urllib.request


def dictionary_of_list_of_dictionaries():
    """Export all tasks from all employees to a JSON file."""
    base = "https://jsonplaceholder.typicode.com"
    users_resp = urllib.request.urlopen("{}/users".format(base))
    users = json.loads(users_resp.read().decode("utf-8"))

    todos_resp = urllib.request.urlopen("{}/todos".format(base))
    todos = json.loads(todos_resp.read().decode("utf-8"))

    usernames = {user.get("id"): user.get("username") for user in users}

    data = collections.OrderedDict()
    for user in users:
        data[str(user.get("id"))] = []

    for task in todos:
        user_id = str(task.get("userId"))
        data[user_id].append({
            "username": usernames.get(task.get("userId")),
            "task": task.get("title"),
            "completed": task.get("completed")
        })

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    dictionary_of_list_of_dictionaries()

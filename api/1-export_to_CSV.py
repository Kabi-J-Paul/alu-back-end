#!/usr/bin/python3
"""Export an employee's TODO list data to CSV format."""
import csv
import json
import sys
import urllib.request


def export_to_CSV(user_id):
    """Export all tasks owned by the employee to a CSV file."""
    base = "https://jsonplaceholder.typicode.com"
    user_resp = urllib.request.urlopen(
        "{}/users/{}".format(base, user_id))
    user = json.loads(user_resp.read().decode("utf-8"))

    todos_resp = urllib.request.urlopen(
        "{}/todos?userId={}".format(base, user_id))
    todos = json.loads(todos_resp.read().decode("utf-8"))

    username = user.get("username")

    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
        for task in todos:
            writer.writerow([user_id, username, task.get("completed"),
                             task.get("title")])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    export_to_CSV(sys.argv[1])

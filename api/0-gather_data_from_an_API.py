#!/usr/bin/python3
"""Gather data from an API for a given employee TODO list progress."""
import json
import sys
import urllib.request


def gather_data_from_an_api(user_id):
    """Return TODO list progress for a given employee ID."""
    base = "https://jsonplaceholder.typicode.com"
    user_resp = urllib.request.urlopen(
        "{}/users/{}".format(base, user_id))
    user = json.loads(user_resp.read().decode("utf-8"))

    todos_resp = urllib.request.urlopen(
        "{}/todos?userId={}".format(base, user_id))
    todos = json.loads(todos_resp.read().decode("utf-8"))

    name = user.get("name")
    done_tasks = [t.get("title") for t in todos if t.get("completed")]
    total = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done_tasks), total))
    for title in done_tasks:
        print("\t {}".format(title))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    gather_data_from_an_api(sys.argv[1])

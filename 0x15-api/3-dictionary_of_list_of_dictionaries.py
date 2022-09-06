#!/usr/bin/python3
"""
3. Dictionary of list of dictionaries
"""
import json
import requests


if __name__ == "__main__":
    """
    Main
    """
    url = "https://jsonplaceholder.typicode.com/"
    allUsers = requests.get("{}users".format(url)).json()
    jsonFile = "todo_all_employees"
    obj = {}
    for user in allUsers:
        uid = user.get("id")
        username = user.get("username")
        todoListRequest = requests.get("{}users/{}/todos".format(url, uid)).json()
        row = [{"username": username,
              "task": tdlr.get("title"),
              "completed": tdlr.get("completed"),
              } for tdlr in todoListRequest]
        obj[uid] = row
    with open("{}.json".format(jsonFile), 'w') as f:
        json.dump(obj, f)

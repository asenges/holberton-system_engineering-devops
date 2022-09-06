#!/usr/bin/python3
"""
1. Export to JSON
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
    Main
    """
    if len(argv) > 1:
        try:
            uid = int(argv[1])
            url = "https://jsonplaceholder.typicode.com/users/"
            userRequest = requests.get("{}/{}".format(url, uid))
            data = userRequest.json()
            if userRequest.json().get("username") is not None:
                todoListRequest = requests.get("{}{}/todos".format(url, uid))
                with open("{}.json".format(uid), 'w', newline='') as f:
                    obj = []
                    for task in todoListRequest.json():
                        obj.append({'task': task.get('title'),
                                    'completed': task.get('completed'),
                                    'username': task.get('username')})
                    file = {'{}'.format(uid): obj}
                    json.dump(file, f)
            else:
                print("User doesn't exists")
        except ValueError:
            print("Please enter the user Id number")
    else:
        print("Please enter the user Id number")

#!/usr/bin/python3
"""
1. Export to CSV
"""
import csv
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
            if userRequest.json().get("username") is not None:
                todoListRequest = requests.get("{}{}/todos".format(url, uid))
                with open("{}.csv".format(uid), 'w', newline='') as f:
                    file = csv.writer(f, quoting=csv.QUOTE_ALL)
                    for task in todoListRequest.json():
                        file.writerow([int(uid),
                                      userRequest.json().get("username"),
                                      task.get('completed'),
                                      task.get('title')])
            else:
                print("User doesn't exists")
        except ValueError:
            print("Please enter the user Id number")
    else:
        print("Please enter the user Id number")

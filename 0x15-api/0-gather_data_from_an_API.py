#!/usr/bin/python3
"""
API connect
"""
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
            if userRequest.json().get("name") is not None:
                todoListRequest = requests.get("{}{}/todos".format(url, uid))
                todoList = todoListRequest.json()
                taskCounter = len(todoList)
                doneTasks = []
                for thisTask in todoList:
                    if thisTask.get("completed") is True:
                        doneTasks.append(thisTask)
                doneTaskCount = len(doneTasks)
                print("Employee {} is done with tasks({}/{}):"
                      .format(userRequest.json().get("name"),
                              doneTaskCount, taskCounter))
                for thisTask in doneTasks:
                    print("\t {}".format(thisTask.get("title")))
            else:
                print("User doesn't exists")
        except ValueError:
            print("Please enter the user Id number")
    else:
        print("Please enter the user Id number")

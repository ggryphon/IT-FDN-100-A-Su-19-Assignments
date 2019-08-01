#!/usr/bin/env python

"""
Assignment 05
Allows a user to manage a to do list
Python 3.7.3
"""

infile = r"C:\_PythonClass\Assignments\hw5\Todo.txt"

# reads ToDo.txt
with open(infile, 'r') as todo_file:
    lines = todo_file.readlines()

# empty dictionary to store data
task_dict = {}

for line in lines:
    task, priority = line.split(",")  # splits the line and pulls out task and priority
    task_dict[task] = priority.replace("\n", "")  # adds key to dictionary using task as key and priority as value

while True:
    print("""
    Menu
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input())
    print()

    # Choice 1 - Shows the current items in the table
    if strChoice == '1':
        print("To Do List:")
        for key in task_dict:
            print(key + ", " + task_dict[key])
        # loops through the dictionary and prints items
    
    # Choice 2 - Add a new item to the list/table
    elif strChoice == '2':
        item_input = input("Item: ")
        if item_input in task_dict:
            print("Item already exists!\n" + item_input + ", " + task_dict[item_input])
            continue
        task_dict[item_input] = input("Priority: ")
        print("Added!")
        # adds a new key, value pair to the dictionary
   
    # Choice 3 - Remove an item from the list/table
    elif strChoice == '3':
        remove_key = input("Enter the task name to remove: ")
        if remove_key in task_dict:
            del task_dict[remove_key]
            print("Task removed!")
        else:
            print("Task does not exist.")
        # deletes a key
   
    # Choice 4 - Save tasks to the ToDo.txt file
    elif strChoice == '4':
        with open(infile, 'w') as todo_file:
            for key in task_dict:
                todo_file.write(key + "," + task_dict[key] + "\n")
        print("Saved to " + infile)
        # loop through dictionary and writes to file
    
    # Choice 5 - End the program
    elif strChoice == '5':
        break
        # ends the program

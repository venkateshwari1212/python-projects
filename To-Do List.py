""" Create a Python program that implements a simple to-do list
manager. The program should allow the user to perform the
following actions:
Add a task: Add a new task to the to-do list.
Remove a task: Remove a task from the to-do list by
specifying its index or name.
Mark a task as done: Mark a specific task as completed.
Display pending tasks: Show all tasks that have not yet
been marked as done.
The program should display a menu with these options, and
the user can choose which action to perform. It should store
the tasks in a list, and each task can be represented by a
dictionary with properties like task name and whether it's
done or not"""

tasks = []

def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Mark a task as done")
    print("4. Display pending tasks")
    print("5. Exit")

def add_task():
    task_name = input("Enter the task: ").strip()
    tasks.append({"name": task_name, "done": False})
    print(f"Task '{task_name}' added.")

def remove_task():
    task_name = input("Enter the task name to remove: ").strip()
    for task in tasks:
        if task["name"].lower() == task_name.lower():
            tasks.remove(task)
            print(f"Task '{task_name}' removed.")
            return
    print("Task not found.")

def mark_task_done():
    task_name = input("Enter the task name to mark as done: ").strip()
    for task in tasks:
        if task["name"].lower() == task_name.lower():
            task["done"] = True
            print(f"Task '{task_name}' marked as done.")
            return
    print("Task not found.")

def display_pending_tasks():
    print("\nPending Tasks:")
    pending_tasks = [task for task in tasks if not task["done"]]
    if not pending_tasks:
        print("No pending tasks.")
    else:
        for task in pending_tasks:
            print(f"- {task['name']}")

while True:
    display_menu()
    choice = input("Choose an option (1-5): ").strip()
    
    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        display_pending_tasks()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

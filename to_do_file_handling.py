# William Stempka

import json


def load_tasks():
    """Loads the file """
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            return tasks
    except:
        with open("tasks.json", "r") as file:
            tasks = []
            json.dumps(tasks, indent=4)
        return tasks


def display_complete_tasks(tasks):
    """Shows all tasks that are complete"""
    for i in tasks:
        if i["status"] == "complete":
            print(f"ID: {i["id"]} \n Description: {i["description"]}")
        else:
            print("No tasks are completed")


def display_incomplete_tasks(tasks):
    """Shows all tasks that are incomplete"""
    for i in tasks:
        if i["status"] == "incomplete":
            print(f"ID: {i["id"]} \n Description: {i["description"]}")
        else:
            print("No tasks are incompleted")


def save_tasks(tasks):
    """will save changes to the file"""
    with open("tasks.json", "w") as file:
        file.write(json.dumps(tasks, indent=4))


def display_tasks(tasks):
    """Shows all the tasks that are in the file and their information"""
    for i in tasks:
        if i["status"] == "incomplete" or i["status"] == "complete":
            print(f"ID: {i["id"]}")
            print(f"Description: {i["description"]}")
            print(f"Status: {i["status"]}")


def add_task(tasks):
    """Adds a task to the file """
    task_id = input("Enter a unique task ID: ").upper()
    task_description = input("Enter the task description: ")
    file = open("tasks.json", "a")
    tasks.append({"id": task_id})
    tasks.append({"description": task_description})
    tasks.append({"status": "incomplete"})
    save_tasks(tasks)
    print("Task added successfully!")


def mark_task_complete(tasks):
    """Changes a task from incomplete to complete"""
    task_id = input("Enter the ID of the task to mark complete: ")
    for i in range(0, len(tasks)):
        if tasks[i]["id"] == task_id:
            tasks[i]["status"] = "complete"
            save_tasks(tasks)
            print(f"Task {tasks[i]["description"]} marked as complete!")


def main():
    """Loop through file options"""
    tasks = load_tasks()
    while True:
        resp = input(
            "Please choose an option \n1. View completed tasks \n2. View incomplete tasks \n3. View all tasks \n4. Mark a task as complete \n5. Add a new task \n6. Exit \n")
        if resp == "1":
            display_complete_tasks(tasks)
        elif resp == "2":
            display_incomplete_tasks(tasks)
        elif resp == "3":
            display_tasks(tasks)
        elif resp == "4":
            mark_task_complete(tasks)
        elif resp == "5":
            add_task(tasks)
        elif resp == "6":
            print("Goodbye! All tasks have been saved.")
            break


if __name__ == "__main__":
    main()

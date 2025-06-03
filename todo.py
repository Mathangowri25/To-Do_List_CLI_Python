import argparse
import json
import os

TASKS_FILE = 'tasks.json'

# Load existing tasks from JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "description": description}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        print(f"{task['id']}: {task['description']}")

# Update a task
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            save_tasks(tasks)
            print(f"Task {task_id} updated.")
            return
    print(f"Task {task_id} not found.")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(updated_tasks) == len(tasks):
        print(f"Task {task_id} not found.")
    else:
        save_tasks(updated_tasks)
        print(f"Task {task_id} deleted.")

# Argument parser setup
def main():
    parser = argparse.ArgumentParser(description="Simple CLI To-Do List Manager")
    subparsers = parser.add_subparsers(dest='command')

    # Add task
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('description', type=str, help='Task description')

    # View tasks
    subparsers.add_parser('view', help='View all tasks')

    # Update task
    parser_update = subparsers.add_parser('update', help='Update a task')
    parser_update.add_argument('id', type=int, help='Task ID to update')
    parser_update.add_argument('description', type=str, help='New description')

    # Delete task
    parser_delete = subparsers.add_parser('delete', help='Delete a task')
    parser_delete.add_argument('id', type=int, help='Task ID to delete')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'view':
        view_tasks()
    elif args.command == 'update':
        update_task(args.id, args.description)
    elif args.command == 'delete':
        delete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

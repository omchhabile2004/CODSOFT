import json
import os

TODO_FILE = "todo_list.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    task_name = input("Enter the task: ").strip()
    tasks = load_tasks()
    tasks.append({"task": task_name, "status": "Pending"})
    save_tasks(tasks)
    print("Task added successfully!")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return
    print("\nTo-Do List:")
    print("-" * 40)
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} - [{task['status']}]")
    print("-" * 40)

# Mark a task as completed
def mark_completed():
    tasks = load_tasks()
    view_tasks()
    
    try:
        task_number = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task():
    tasks = load_tasks()
    view_tasks()

    try:
        task_number = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            deleted_task = tasks.pop(task_number)
            save_tasks(tasks)
            print(f"Deleted Task: {deleted_task['task']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# User-friendly menu
def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

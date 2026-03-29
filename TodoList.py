tasks = []

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully.")
    else:
        print("Task cannot be empty.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n--- Tasks ---")
    for index, item in enumerate(tasks, 1):
        status = "✓" if item["completed"] else "✗"
        print(f"{index}. [{status}] {item['task']}")

def mark_completed():
    view_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            print(f"Task '{deleted['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n--- Todo List Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

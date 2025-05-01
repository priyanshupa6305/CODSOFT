import os

def show_tasks(tasks):
    print("\n===== To-Do List =====")
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print("Task added successfully.")
    return tasks

def update_task(tasks, index, updated_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = updated_task
        print("Task updated successfully.")
    else:
        print("Invalid task index.")
    return tasks

def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task '{deleted_task}' deleted successfully.")
    else:
        print("Invalid task index.")
    return tasks

def save_tasks_to_file(file_path, tasks):
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")
    print("Tasks saved successfully.")

def load_tasks_from_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read().splitlines()
    return []

def main():
    file_path = "todo_list.txt"
    tasks = load_tasks_from_file(file_path)

    while True:
        print("\n===== To-Do List =====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Save & Exit")
        print("======================")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the task to add: ").strip()
            tasks = add_task(tasks, new_task)
        elif choice == "3":
            try:
                index = int(input("Enter the task index to update: ").strip())
                updated_task = input("Enter the updated task: ").strip()
                tasks = update_task(tasks, index, updated_task)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            try:
                index = int(input("Enter the task index to delete: ").strip())
                tasks = delete_task(tasks, index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "5":
            save_tasks_to_file(file_path, tasks)
            confirm_exit = input("Are you sure you want to exit? (y/n): ").strip().lower()
            if confirm_exit == "y":
                print("Exiting...")
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


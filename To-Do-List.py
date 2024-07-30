import sys

# Dictionary to store tasks
tasks = {}

# Function to add a task
def add_task(task_id, task_description):
    tasks[task_id] = {
        'description': task_description,
        'status': 'Pending'
    }
    print(f"Task '{task_description}' added successfully with ID {task_id}.")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for task_id, info in tasks.items():
        print(f"ID: {task_id}, Description: {info['description']}, Status: {info['status']}")

# Function to update a task
def update_task(task_id, task_description=None, status=None):
    if task_id in tasks:
        if task_description:
            tasks[task_id]['description'] = task_description
        if status:
            tasks[task_id]['status'] = status
        print(f"Task ID {task_id} updated successfully.")
    else:
        print("Task not found.")

# Function to delete a task
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task ID {task_id} deleted successfully.")
    else:
        print("Task not found.")

# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

# Main function to run the application
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            task_id = input("Enter task ID: ")
            task_description = input("Enter task description: ")
            add_task(task_id, task_description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = input("Enter task ID to update: ")
            task_description = input("Enter new task description (leave blank to keep current): ")
            status = input("Enter new status (Pending/Completed) (leave blank to keep current): ")
            update_task(task_id, task_description, status)
        elif choice == '4':
            task_id = input("Enter task ID to delete: ")
            delete_task(task_id)
        elif choice == '5':
            print("Exiting the program.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

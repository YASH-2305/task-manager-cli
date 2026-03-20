from database.db import create_tables
from database.task_db import add_task, view_tasks, mark_completed, delete_task

def main():
    create_tables()

    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            add_task(title, deadline)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            mark_completed(task_id)

        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            delete_task(task_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
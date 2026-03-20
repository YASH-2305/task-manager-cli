from database.db import connect_db

def add_task(title, deadline):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, deadline) VALUES (?, ?)",
        (title, deadline)
    )

    conn.commit()
    conn.close()
    print("Task added successfully!")

def view_tasks():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()

    print("\n===== Your Tasks =====")
    for task in tasks:
        print(f"""
ID: {task[0]}
Title: {task[1]}
Status: {task[2]}
Created At: {task[3]}
Deadline: {task[4]}
--------------------------
""")

def mark_completed(task_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status = 'completed' WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()
    print("Task marked as completed!")

def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()
    print("Task deleted!")
# Beginner Level Project To Make a "TO-DO LIST" In Python.

def add_task(tasks):
    add = input("Enter task you want to add: ")
    tasks.append(add)
    print(f"Task '{add}' has been successfully added...")

def update_task(tasks):
    updated_val = input("Enter the task you want to update: ")
    if updated_val in tasks:
        up = input("Enter new task: ")
        ind = tasks.index(updated_val)
        tasks[ind] = up
        print(f"Updated task to: {up}")
    else:
        print(f"Task '{updated_val}' not found!")

def delete_task(tasks):
    del_val = input("Which task do you want to delete? ")
    if del_val in tasks:
        tasks.remove(del_val)
        print(f"Task '{del_val}' has been deleted...")
    else:
        print(f"Task '{del_val}' not found!")

def view_tasks(tasks):
    if tasks:
        print(f"Total tasks: {tasks}")
    else:
        print("No tasks available!")

def task_manager():
    tasks = []  # empty list
    print("---WELCOME TO THE TASK MANAGEMENT APP---")

    try:
        total_task = int(input("Enter how many tasks you want to add: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    for i in range(1, total_task + 1):
        task_name = input(f"Enter Task {i}: ")
        tasks.append(task_name)
    print(f"Today's tasks are:\n{tasks}")

    while True:
        try:
            operation = int(input("\nEnter: \n1 - Add Task\n2 - Update Task\n3 - Delete Task\n4 - View Tasks\n5 - Exit Program\nYour choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if operation == 1:
            add_task(tasks)
        elif operation == 2:
            update_task(tasks)
        elif operation == 3:
            delete_task(tasks)
        elif operation == 4:
            view_tasks(tasks)
        elif operation == 5:
            print("Closing the program...")
            break
        else:
            print("INVALID INPUT!!!")

task_manager()

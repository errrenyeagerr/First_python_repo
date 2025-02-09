# First Beginner-level project to make a TO-DO LIST in python.

def task():
    tasks = [] #empty list
    print("---WELCOME TO THE TASK MANAGEMENT APP---")

    total_task = int(input("Enter how many times you want to add = "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter Task {i} = ")
        tasks.append(task_name)
    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1 - Add Task\n2 - Update Task\n3 - Delete\n4 - View Tasks\n5 - Exit Program."))

        if operation == 1:
            add = input("Enter task you want to add : ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task you want ro update : ")
            if updated_val in tasks:
                up = input ("Enter new task =")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {up}")

            elif operation == 3:
                del_val = input("Which task you want to delete?? ")
                if del_val in tasks:
                    ind = tasks.index(del_val)
                    del tasks[ind]
                    print(f"Task {del_val} has been deleted...")

            elif operation == 4:
                print(f"Total tasks : {tasks}")

            elif operation == 5:
                print("Closing the program...")
                break

            else:
                print("INVALID INPUT!!!")

task()
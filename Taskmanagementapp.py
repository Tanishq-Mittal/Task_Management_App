def task():
    tasks = []  # empty task
    print("-----Welcome to the Task Management App-----")

    total_task = int(input("Enter how many task you want to add = "))

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Options are : \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\nEnter your choice = "))

        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")

            if updated_val in tasks:
                up = input("Enter new task : ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {up}")
            else:
                print("Task not found...")

        elif operation == 3:
            delete_val = input("Enter task you want to delete = ")

            if delete_val in tasks:
                tasks.remove(delete_val)
                print(f"Task {delete_val} has been deleted...")
            else:
                print("Task not found...")

        elif operation == 4:
            print(f"Today's tasks are\n{tasks}")

        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid Input")

task()
# Project 2: To-Do List Application
# Description: Build a command-line to-do list application where
# users can add, delete, and view tasks.
# Skills: Lists, loops, user input, file handling


def To_Do_list():

    print("\n---------To Do List-------------")

    task = []
    daily_task = int(input("Enter How Many Task You Went to add! "))
    for i in range(1, daily_task + 1):
        task_name = input(f"Please Enter the Task {i} ")
        task.append(task_name)
    print(f"To Day all Task {task} ")

    while True:
        print("1.Enter the add task ")
        print("2.Update Task ")
        print("3.Delete the task ")
        print("4.View the add task ")
        print("5.Exit")
        Choies = int(input("Enter the Number According your Chiese! "))
        if Choies == 1:
            add = input("Enter The Task: ")
            task.append(add)
            print("Task SuccsFull Add! ")
        elif Choies == 2:
            up_value = input("Enter the task for Update ")
            if up_value in task:
                new = input("Enter new task ")
                id = task.index(up_value)
                task[id] = new
                print(f"Update Task {new} ")

        elif Choies == 3:
            del_task = input("Enter the Task You can remove ")
            print(task)
            if del_task in task:
                ind = task.index(del_task)
                del task[ind]
                print("Remove Task! ")
        elif Choies == 4:
            print(task)

        elif Choies == 5:
            print("Good By Thank You for Using my App! ")
            break


To_Do_list()

"""
Author: Noah Yue
Email: jackwade050802@gmai.com
Date: 2024-2-21
Description: To-do list task
"""
# add will conflict with delete since add will detect the lens of dic. But when delete one the len will -1
# and make prog. error. so use a new variable call taskid to keep following id will not affect by lens.


# add task
def add(desc, next_id):
    tasks[next_id] = (desc, "not finished")
    return tasks


# view task
def view(tdl):
        if len(tdl) == 0:
            print("No tasks to show.")
            return 0
        for task_id, (desc, status) in tdl.items():
            print(task_id, desc, "-", status)


# Mark task
def mark(taskid):
    if taskid in tasks:
        descript = tasks[taskid][0]
        tasks[taskid] = (descript, "finished")
        print(taskid, "is marked as completed.")
    else:
        print("Task ID does not exist.")


# delete task
def delete(taskid):
    if taskid in tasks:
        del tasks[taskid]
        print("Task", taskid, "deleted.")
    else:
        print("Task", taskid, " does not exist.")


tasks = {}
taskID = 1
while True:
    print("\nTo-Do List Application\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Mark Task\n5.Exit\n")
    choice = input("Enter your choice: ")
# add new task
    if choice == "1":
        description = input("\nEnter task description: ")
        add(description, taskID)
        taskID += 1
# view all exist task
    elif choice == "2":
        view(tasks)
# delete one task
    elif choice == "3":
            ID = int(input("\nEnter task ID to delete: "))
            delete(ID)
# mark as accomplished
    elif choice == "4":
            ID = int(input("\nEnter task ID to mark as completed: "))
            mark(ID)
# exit
    elif choice == "5":
        print("Exiting application.")
        break

    else:
        print("Invalid choice. Please choose a valid option.")

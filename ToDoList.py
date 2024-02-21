#Programmed Task List (allows user to add, complete, delete, and view tasks)
tasks = {}  #opening an empty dictionary

#prompting user to follow directions and input choice

print("Enter one of the following commands:\n[A] Add new tasks.\n[B] View all tasks.\n[C] Complete task.\n[D] Delete tasks.\n[E] End program.")
ans = input()

#while the user does not wish to end program

while ans != "E":

    if ans == "A": #adding tasks
        temp = input("Enter a new task: ")
        tasks[temp] = False

    elif ans == "B": #viewing tasks
        print("Tasks:")
        count = 1
        sorted_tasks = sorted(tasks.items()) #program to sort the tasks alphabetically
        for task, completed in sorted_tasks:
            status = "complete" if completed else "incomplete" #announce status of task
            print(f"{count}. {task} is {status}")
            count += 1

    elif ans == "C": #completing tasks
        print("Enter completed task:")
        temp = input()
        if temp in tasks:
            tasks[temp] = True
        else: #if invalid answer entered
            print("Task not found.")

    elif ans == "D": #deleting tasks
        print("Enter deleted task:")
        temp = input()
        if temp in tasks:
            tasks.pop(temp)
        else: #if invalid answer entered
            print("Task not found.")

    print("\nEnter one of the following commands:\n[A] Add new tasks.\n[B] View all tasks.\n[C] Complete task.\n[D] Delete tasks.\n[E] End program.") #continue running through tasks/program until E is entered
    ans = input()
            
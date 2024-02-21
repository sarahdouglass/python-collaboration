tasks = {}

print("Enter one of the following commands:\n[A] Add new tasks.\n[B] View all tasks.\n[C] Complete task.\n[D] Delete tasks.\n[E] End program.")
ans = input()

while ans != "E":
    if ans == "A": 
        temp = input("Enter a new task: ")
        tasks[temp] = False
    elif ans == "B":
        print("Tasks:")
        count = 1
        sorted_tasks = sorted(tasks.items())
        for task, completed in sorted_tasks:
            status = "complete" if completed else "incomplete"
            print(f"{count}. {task} is {status}")
            count += 1
    elif ans == "C":
        print("Enter completed task:")
        temp = input()
        if temp in tasks:
            tasks[temp] = True
        else:
            print("Task not found.")
    elif ans == "D":
        print("Enter deleted task:")
        temp = input()
        if temp in tasks:
            tasks.pop(temp)
        else:
            print("Task not found.")

    print("\nEnter one of the following commands:\n[A] Add new tasks.\n[B] View all tasks.\n[C] Complete task.\n[D] Delete tasks.\n[E] End program.")
    ans = input()
            
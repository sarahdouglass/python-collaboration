tasks = {}

print("Enter one of the following commands:\n[A]Add new tasks.\n[B]View all tasks.\n[C]Complete task.\n[D]Delete tasks.\n[E]End program.")
ans = input()

while ans != "E":
    if(ans == "A"): 
        temp = input("Enter a new task:")
        tasks.update({temp:False})
    elif(ans == "B"):
        print("Tasks:")
        count = 1
        for task,completed in tasks.items():
            if completed: status = "complete"
            else: status = "incomplete"
            print(f"{count}. {task} is {status}")
            count += 1
    elif(ans == "C"):
        print("Enter completed task.")
        temp = input()
        tasks.update(temp,True)
    elif(ans == "D"):
        print("Enter deleted task.")
        temp = input()
        tasks.pop(temp)
    
    print("Enter one of the following commands:\n[A]Add new tasks.\n[B]View all tasks.\n[C]Complete task.\n[D]Delete tasks.\n[E]End program.")
    ans = input()
            
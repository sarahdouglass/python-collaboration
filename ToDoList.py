tasks = {}

print("Enter one of the following commands:\n[A]Add new tasks.\n[B]View all tasks.\n[C]Complete task.\n[D]Delete tasks.\n[E]End program.")
ans = input()

while ans != "E":
    if(ans == "A"): 
        temp = input("Enter a new task:")
        tasks.update({temp:False})
    elif(ans == "B"):
        keys = tasks.keys()
        vals = tasks.values()
        print("Tasks:")
        count = 1
        for task,completed in tasks.items():
            if completed: status = "complete"
            else: status = "incomplete"
            print(f"{count}. {task} is {status}")
            count += 1
    elif(ans == "C"):
        keys = tasks.keys()
        for i in range(len(keys)):
            print(i,". ", keys[i])
        print("Enter number for completed task.")
        num = int(input())
        tasks.update(keys[num + 1])
    elif(ans == "D"):
        keys = tasks.keys()
        for i in range(len(keys)):
            print(i,". ", keys[i])
        print("Enter number for deleted task.")
        num = int(input())
        tasks.pop(keys[num+1])
    
    print("Enter one of the following commands:\n[A]Add new tasks.\n[B]View all tasks.\n[C]Complete task.\n[D]Delete tasks.\n[E]End program.")
    ans = input()
            
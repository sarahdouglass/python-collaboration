tasks = {}

print("Enter one of the following commands:\n[A]Add new tasks.\n[B]View all tasks.\n[C]Complete task.\n[D]Delete tasks.\n[E]End program.")
ans = input()

while ans != "E":
    if(ans == "A"): 
        temp = input("Enter a new task:")
        tasks.update({temp:False})
    elif(ans == "B"):
        keys = tasks.keys()
        print("Tasks:")
        for i in range(len(keys)):
            if(tasks.get(keys[i])): print(i,". ", keys[i], "is completed.")
            else:print(i,". ", keys[i], "is incomplete.")
    elif(ans == "C"):
        keys = tasks.keys()
        for i in range(len(keys)):
            print((i+1),". ", keys[i])
        print("Enter number for completed task.")
        num = int(input())
        tasks.update(keys[num + 1])
    elif(ans == "D"):
        keys = tasks.keys()
        for i in range(len(keys)):
            print((i+1),". ", keys[i])
        print("Enter number for deleted task.")
        num = int(input())
        tasks.pop(keys[num+1])
    
    print("Enter one of the following commands:\n[A]Add new tasks.\n[B]View all tasks.\n[C]Complete task.\n[D]Delete tasks.\n[E]End program.")
    ans = input()
            
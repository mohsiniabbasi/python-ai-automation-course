todo = []
while True:
    choice = input("add / show / remove / quit: ")
    if choice == "quit":
        break
    elif choice == "add":
        task = input ("what needs doing: ")
        todo.append(task)
        print("added", task)
    elif choice == "show":
        print(todo)
    elif choice == "remove":
        task = input("which one to remove: ")
        if task in todo:
            todo.remove(task)
            print("removed:", task)
        else:
            print("This is not in the list")
    else:
        print("I don't know that one")


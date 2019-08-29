

def deleteTask():
    choreList = ["dish", "clothes", "car"]
    userInput = input("what task do you want to delete")
    for i in choreList:
        if userInput == i:
            choreList.remove(userInput)
    print(choreList)

# arrayOfTasks.remove(deleteTask)


deleteTask()


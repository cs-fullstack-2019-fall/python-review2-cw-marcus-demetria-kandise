from Kandice import userInput


def deleteTask():
    if userInput == 3:
        choreList = ["dish", "clothes", "car"]
        print(choreList)
        userInput2 = input("what task do you want to delete ")
        for i in choreList:
            if userInput2 == i:
                choreList.remove(userInput2)
        print(choreList)

# arrayOfTasks.remove(deleteTask)


deleteTask()

from Kandice import userInput
from Demetria import tlist
choreList = tlist
def deleteTask():
    if userInput == 3:
        print(choreList)
        userInput2 = input("what task do you want to delete ")
        for i in choreList:
            if userInput2 == i:
                choreList.remove(userInput2)
        print(choreList)
# arrayOfTasks.remove(deleteTask)
deleteTask()
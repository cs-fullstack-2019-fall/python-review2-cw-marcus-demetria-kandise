
from Demetria import tlist
# Congratulations! You're running [YOUR NAME]'s Task List program.

# What would you like to do next?
# 1. List all tasks.
# 2. Add a task to the list.
# 3. Delete a task.
# 0. To quit the program


name = input("Enter your name? ")

def main():

    print(f"Congratulations! You're running {name}'s Task List program\n")
    print(f'What would you like to do next?\n'
          f'1. List all tasks.\n'
          f'2. Add a task to the list.\n'
          f'3. Delete a task.\n'
          f'0. To quit the program')
main()

userInput=int(input("Please make a selection "))
arrayOfName =tlist



def currentTasks():
    # userInput = ""
    if userInput == 1:
        print(f'{name} current task list: {tlist}')





currentTasks()

def addFunction():
    # userInput = ""
    if userInput == 2:
        print(f'Items currently in your list: {arrayOfName}')
        arrayOfName.append(input("Add item to your list: "))
        print(f'Your current list is:{arrayOfName}')
addFunction()



def quitFuncion():
    userInput=""
    while userInput != 0:
        userInput= int(input("Please make a selection "))

quitFuncion()
import sys, os
from PrintMenu import printMenu, validateMenu

def main(args):

    finishedTasks = set()
    pendingTasks = set()
    condition = True
    while condition:
        os.system('cls' if os.name=="nt" else "clear")
        printMenu()
        option = input("Please choose an option: ")

        if not validateMenu(option):
            print("Invalid option.")

        #SHOW LIST
        if int(option) == 0:
            print(pendingTasks)
        
        #ADD TO LIST
        if int(option) == 1:
            pendingTasks.add(input("Input a new task to add: "))

        #SEARCH ON LIST
        if int(option) == 2:
            if input("Input an entry to search: ") in pendingTasks:
                print("The task was found!")
            else:
                print("The task wasn't found.")

        #ERASE FROM LIST
        if int(option) == 3:
            elementToErase = input("Input a task to erase: ")
            if elementToErase in pendingTasks:
                pendingTasks.remove(elementToErase)
                print("Erased successfully!")
            else:
                print("Task wasn't found.")

        #MODIFY FROM LIST
        if int(option) == 4:
            elementToErase = input("Input a task to modify: ")
            if elementToErase in pendingTasks:
                pendingTasks.remove(elementToErase)
                pendingTasks.clear()
                pendingTasks.add(input("Input new task: "))
            else:
                print("Task wasn't found.")

        #CLEAR LIST
        if int(option) == 5:
            pendingTasks.clear()
            print("Tasklist cleared successfully!")

        #ORGANIZE LIST
        if int(option) == 6:
            organisedList=list(pendingTasks)
            organisedList.sort()
            print(organisedList)

        #SHOW COMPLETED TASKS
        if int(option) == 7:
            print(finishedTasks)

        #SHOW INCOMPLETE TASKS
        if int(option) == 8:
            print(pendingTasks)

        #MARK TASK AS COMPLETED
        if int(option) == 9:
            setAsCompleted = input("Please input a task to set as completed: ")
            if setAsCompleted in pendingTasks:
                pendingTasks.remove(setAsCompleted)
                finishedTasks.add(setAsCompleted)
            else:
                print("The task wasn't found.")

if __name__ == '__main__':
    main(sys.argv)

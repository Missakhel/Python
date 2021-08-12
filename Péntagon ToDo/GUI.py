import tkinter
from tkinter import * #Importing standard widgets
from tkinter import ttk
from tkinter.font import Font #Importing ttk for new widgets


#DEFINING MAIN APP WINDOW
root = Tk()
#DEFINING MAIN APP WINDOW DIMENSIONS
root.geometry('300x300')
#CHANGING WINDOW TITLE
root.title('Péntagon ToDo')
#CHANGING WINDOW BG COLOR
root.configure(bg='#252525')

def printTitle(string):
    #Setting up a frame
    mainFrame.destroy()
    frame = Frame(root)
    title = StringVar()
    title.set(string)
    label = Label(frame, textvariable=title, bg='#252525',fg='#ffffff', font=('FreeSans', 24))
    label.place(anchor=NW)
    frame.pack()
    return frame

def add():
    printTitle("Add")

def search():
    printTitle("Search")

def erase():
    printTitle("Erase")

def modify():
    printTitle("Modify")

def organize():
    printTitle("Organize")

def clear():
    printTitle("Clear")

def showAll():
    printTitle("Show All")

def showCompleted():
    printTitle("Show Completed")

def showIncomplete():
    printTitle("Show Incomplete")

    #CREATING A CASCADE MENU
def main():
    frame = Frame(root)
    menuBar = Menu(root)
    taskMenu = Menu(menuBar, tearoff=0)
    taskMenu.add_command(label="Add", command=add)
    taskMenu.add_command(label="Search", command=search)
    taskMenu.add_command(label="Erase", command=erase)
    taskMenu.add_command(label="Modify", command=modify)
    taskMenu.add_command(label="Organize", command=organize)

    taskMenu.add_separator()

    taskMenu.add_command(label="Show All", command=showAll)
    taskMenu.add_command(label="Show Completed", command=showCompleted)
    taskMenu.add_command(label="Show Incomplete", command=showIncomplete)

    taskMenu.add_separator()

    taskMenu.add_command(label="Clear", command=clear)

    taskMenu.add_separator()

    taskMenu.add_command(label="Exit", command=root.quit)
    menuBar.add_cascade(label="Tasklist", menu=taskMenu)

    #Setting up Menu Bar in App
    root.config(menu=menuBar)
    return frame

mainFrame = main()
mainFrame.pack()
root.mainloop()

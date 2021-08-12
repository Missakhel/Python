import tkinter as tk
from tkinter import * #Importing standard widgets

def updater(string):
    for widget in mainFrame.winfo_children():
        widget.destroy()
    Label(mainFrame,
          text=string,
          bg='#252525',
          fg='#ffffff',
          font=('FreeSans', 24)).pack(anchor=NW)
    mainFrame.pack(fill="both", expand=True)

def entryAdder():
    pendingTasks.add(str(option.get())) #not working
    

def add():
    updater("Add")
    Label(mainFrame, text="New Task", background="#252525", fg="#ffffff").pack(side=LEFT)
    Entry(mainFrame, bd=2, background="#252525", fg="#ffffff").pack(side=LEFT)
    Button(mainFrame, text="Save", background="#252525", fg="#ffffff", command=entryAdder).pack(side=RIGHT)

def search():
    updater("Search")

def erase():
    updater("Erase")

def modify():
    updater("Modify")

def organize():
    updater("Organize")

def clear():
    updater("Clear")

def showAll():
    updater("Show All")

def showCompleted():
    updater("Show Completed")

def showIncomplete():
    updater("Show Incomplete")

    #CREATING A CASCADE MENU
def main():
    frame = Frame(root, background="#252525")
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


#DEFINING MAIN APP WINDOW
root = Tk()
#DEFINING MAIN APP WINDOW DIMENSIONS
root.geometry('300x300')
#CHANGING WINDOW TITLE
root.title('Péntagon ToDo')
#CHANGING WINDOW BG COLOR
root.configure(bg='#252525')
#APP INITIALIZATION

option=StringVar()
pendingTasks=set()

mainFrame = main()
mainFrame.pack()
root.mainloop()

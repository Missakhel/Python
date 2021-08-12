def printMenu():
    print("00 | Show tasklist")
    print("01 | Add to tasklist")
    print("02 | Search on tasklist")
    print("03 | Erase from tasklist")
    print("04 | Modify from tasklist")
    print("05 | Clear tasklist")
    print("06 | Organize tasklist")
    print("07 | Show completed tasks")
    print("08 | Show incomplete tasks")
    print("09 | Mark as finished task")
    print("10 | Open task")
    print("11 | Exit app")

def validateMenu(option):
    if int(option)<0 or int(option)>11:
        return False
    return True
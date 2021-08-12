stateMatrix = [
    [9,1,4,9,2,8,4,9,9,1,10],    
    [5,9,8,4,2,9,4,1,9,1,10],
    [5,7,2,1,6,0,1,5,7,1,10],
    [4,9,2,3,2,0,9,1,3,9,10],
    [10,7,8,8,9,6,1,5,7,9,10],
    [5,1,4,6,9,0,9,0,5,1,10],
    [5,7,4,8,6,0,7,5,7,6,10],
    [9,1,2,6,1,9,2,10,2,7,10],
    [4,1,4,7,6,0,7,8,10,7,10],
    [5,4,7,6,9,6,7,5,3,6,10]
]
#   ANGRY           HAPPY           SCARED          SAD             PENSATIVE       ANNOYED       BORED              TIRED           SICK            NEUTRAL   {    DEAD
emotion = 1
action = 0
actionDict = {"Eat":0, "Bathe":1, "Play":2, "Sleep":3, "Walk":4, "Interact":5, "Clean":6, "Explore":7, "Exercise":8, "Study":9}
stateList = ["ANGRY", "HAPPY", "SCARED", "SAD", "PENSATIVE", "ANNOYED", "BORED", "TIRED", "SICK", "NEUTRAL"]
while emotion < 10:
    print(f"Your pet is {stateList[emotion]}")
    print("AVAILABLE ACTIONS")
    for key, value in actionDict.items():
        print(f"[{value}] {key}")
    action = int(input("PLEASE INPUT A NUMBER TO DO THE FOLLOWING ACTIONS: ")) - 1
    emotion = stateMatrix[action][emotion]
print("YOUR PET IS DEAD.")
text = str(input("Input text: "))
isPalindrome = True
spacefree = []

text = text.lower()

for x in text:
    if(x != " "):
        spacefree.append(x)

length=len(spacefree)
counter = int(length/2)

for i in range (counter):
    if(spacefree[i] != spacefree[length-1-i]):
        isPalindrome=False
        break

if(isPalindrome==False):
    print("It isn't a palindrome")
else:
    print("It's a palindrome")

#https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    array1 = []
    array2 = []

    def medianFinder(self,splitString):
        median = 0
        sortedArray = []
        for part in splitString: sortedArray.append(int(part))
        medianRadius = len(sortedArray) // 2

        if (len(sortedArray) % 2 == 1):
            median = sortedArray[medianRadius]
        else:
            median = (sortedArray[medianRadius] + sortedArray[medianRadius - 1]) / 2
        return median

    def parser(self,string1,string2):
        stringX = string1 + "," + string2
        stringX.strip()
        stringX = stringX.split(",")
        stringX.sort()
        median = self.medianFinder(stringX)
        return median

def main():
    instance =  Solution()
    instance.array1 = input("Please input a list numbers separated by commas: ")
    instance.array2 = input("Please input another list of numbers separated by commas: ")

    result = instance.parser(instance.array1,instance.array2)
    print("The median is: ",result)

if __name__ == "__main__":
    main()

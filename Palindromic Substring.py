#https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, string: str) -> str:
        longestPalindrome = ""
        newPalindrome = ""

        for index in range(len(string)):
            if(index > 0 and index < len(string)-1):
                # A palindrome could be even
                if (string[index] == string[index+1] or index == 1  and string[index] == string[index-1]):
                    newPalindrome = self.palindromeBuilding(string, index, 1)
                # Checking if a palindrome is odd
                elif (string[index+1] == string[index-1]):
                    newPalindrome = self.palindromeBuilding(string, index, 0)
            if (len(newPalindrome) > 0 and len(newPalindrome) > len(longestPalindrome)):
                longestPalindrome = newPalindrome
        return longestPalindrome

    #Mode indicates whether the palindrome is ever (0) or odd (1)
    def palindromeBuilding(self, string, index, mode):
        subcharArray = []
        radius = 0
        newPalindrome = ""

        if (index < len(string)-1):
            if(mode == 1):
                newPalindrome = string[index]*2
            else:
                newPalindrome = string[index]

            if (index+mode < len(string)-1):
                radius += 1
                while (string[index-radius] == string[index+radius+mode]):
                    subcharArray.append(string[index-radius])
                    subcharArray.append(string[index+radius+mode])
                    newPalindrome = newPalindrome.join(subcharArray)
                    radius +=1

                    if (index+mode+radius >= len(string) or index-radius < 0):
                        break
                    else:
                        subcharArray.clear()
        return newPalindrome

def main():
    solution = Solution()
    word = input("Please input a word: ").lower()
    word = word.replace(" ","")
    palindrome = solution.longestPalindrome(word)
    print ("The longest palindrome within your text is:", palindrome)

if __name__ == "__main__":
    main()

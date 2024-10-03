class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqDict = {}
        counter = 0
        for x in s:
            if x in freqDict.keys(): #has already been added (was count of 1 now 2)
                del freqDict[x] #remove from dictionary as has pair
                counter +=2
            else:
                freqDict.update({x: 1}) #add to dictionary with count 1
        for y in freqDict:
            if freqDict[y] == 1: #if there is an unmatched letter
                counter+=1 #counts as the middle letter xxxxYxxxx 
                break #break as counting length of longest not number of total palindromes
        return counter

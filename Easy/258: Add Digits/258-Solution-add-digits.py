class Solution:

    def addDigits(self, num: int) -> int:
        strNum = str(num)
        counter = 0
        if len(strNum) == 1: #if only one character... BASE CASE
            return num
        for i in range (len(strNum)) :#for every digit... RECURSIVE CASE
            counter += int(strNum[i]) #add together
        return self.addDigits(counter) #recursive GOTO line 4

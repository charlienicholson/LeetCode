class Solution:
    def romanToInt(self, s: str) -> int:
        individualVals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        romanInt = 0
        x = 0
        while x <= (len(s)-1):
            currentVal = individualVals.get(s[x]) #current int<->char equivalent
            if(x == (len(s)-1)): #final char value is not part of pair
                romanInt += currentVal
                return romanInt #also early ret for s of 1
            futureVal = individualVals.get(s[(x+1)]) #next int<->char equivalent
            if(currentVal < futureVal): #special deductive operation. e.g. IV
                romanInt+=futureVal
                romanInt-=currentVal
                x += 2 #increment to skip the pair's second value
                continue
            romanInt += currentVal #not special nor last
            x+=1
        return romanInt

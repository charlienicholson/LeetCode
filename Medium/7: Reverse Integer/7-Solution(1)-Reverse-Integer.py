class Solution:
    def classifer(self,x):
        if x<-(2**31) or x>2**31 - 1: #x is too big -> ret 1
            return 1
        elif(x>=0): #x is positive -> ret 2
            return 2
        else: #x is negative -> ret 3
            return 3

    def reverse(self, x: int) -> int:
        match self.classifer(x): #What category is x in?
            case 1:
                return 0              
            case 2:
                x= str(x)[::-1] #flip
            case 3:
                x = "-" + str(x)[1:][::-1] #adds a - to a cut and flipped 

        if self.classifer(int(x)) > 1: #checks again to see if post flip it's too big
            return int(x)
        else:
            return 0


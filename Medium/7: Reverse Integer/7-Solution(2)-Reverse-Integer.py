class Solution:
    def classifier(self,x):

        if(x>=0): #x is positive -> ret 2
            x= str(x)[::-1] 
        else: #x is negative -> ret 3
            x = "-" + str(x)[1:][::-1]
        if int(x)<-(2**31) or int(x)>2**31 - 1: 
            return 0
        else:
            return int(x)

    def reverse(self, x: int) -> int:
        return(self.classifier(x))
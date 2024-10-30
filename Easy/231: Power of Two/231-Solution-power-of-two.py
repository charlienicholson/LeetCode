class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0
        finished = False
        while(2**power <= n):
            if(2**power == n):
                return True
            power+=1
        return False

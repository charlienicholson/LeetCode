class Solution:
    def recursiveNthString(self, start: str, iterations: int) -> str:
        iterations -= 1
        if(iterations == 0):
            return start
        binary =  ''.join('1' if bit == '0' else '0' for bit in start)
        binary = binary[::-1]
        start = start + "1" + binary
        return self.recursiveNthString(start,iterations)
 
    def findKthBit(self, n: int, k: int) -> str:
        fin = self.recursiveNthString("0",n)
        return fin[k-1]

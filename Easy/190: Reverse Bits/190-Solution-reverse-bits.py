class Solution:
    def reverseBits(self, n: int) -> int:     
        nBinary = f'{n:032b}'
        nBinary = str(nBinary)[::-1]
        nBinary = int(nBinary, 2)
        return nBinary
        

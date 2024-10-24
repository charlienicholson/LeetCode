class Solution:
    def binaryFlipper(self, numBinary:str) -> int:
        maskBinary = (1 << len(numBinary)) - 1 #create mask of 1's equivelent to bin str len
        maskBinary = bin(maskBinary)[2:] #remove that 0b at start
        flippedBits=int(numBinary,2) ^ int(maskBinary,2) #xor to flip bits
        return flippedBits
    def findComplement(self, num: int) -> int:
        numBinary = bin(num)[2:]
        return self.binaryFlipper(numBinary)

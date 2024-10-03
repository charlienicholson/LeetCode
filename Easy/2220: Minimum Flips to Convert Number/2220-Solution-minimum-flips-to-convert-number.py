class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #convert ints to binary
        #zfill till they are the same length
        #for each value if they are the same then do nothing if different then add 1 to counter
        #ret counter
        aBin = format(start, 'b')
        bBin = format(goal, 'b')
        #now zfill then convert to int:
        aBin, bBin = aBin.zfill(max(len(aBin), len(bBin))), bBin.zfill(max(len(aBin), len(bBin)))
        counter = 0
        print(len(aBin))
        print(len(bBin))
        for x in range(len(aBin)):
            if(aBin[x] != bBin[x]):
                counter +=1
        return counter

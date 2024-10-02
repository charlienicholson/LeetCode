class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freqDict = {}
        for x in nums:
            if str(x) in freqDict.keys():
                freqDict[str(x)]+=1
            else:
                freqDict.update({str(x): 1})
        return int(list(freqDict.keys())[list(freqDict.values()).index(1)])

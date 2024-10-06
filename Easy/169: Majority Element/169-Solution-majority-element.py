class Solution:
    def majorityElement(self, nums: List[int]) -> int:    
        nums.sort() #order
        n = len(nums) #not really needed but clean
        return nums[n//2] #find median which is most recurring
        """
        More expandable and robust version, sacrifices runtime.
        
        elementDict = {}
        for x in nums:
            if x in elementDict.keys():
                elementDict[x] += 1
                if(elementDict[x] >= (len(nums)/2)):
                    return x
            else:
                elementDict.update({x: 1})
        return x
        """

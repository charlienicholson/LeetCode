class Solution:

    def quantizer(self, mapValues: List[int], item :int) -> int:
        validValues = [m for m in mapValues if m <= item]
        return max(validValues) if validValues else None #quantizes if no vlaue then ret 0

    def getBeauty(self, bestDict: dict, value:int) -> int:
            return bestDict.get(value, 0) #gets from best value dictionary

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        bestValue = [] #store the best beauty to price pairs
        bestPrice = [] #store the prices from best pairs
        for item in items:
            if len(bestValue) == 0: #add first item so cheapest can buy
                bestValue.append(item)
                bestPrice.append(item[0])
                continue
            if(item[1] > bestValue[-1][1]):#greater beauty
                if(item[0] == bestValue[-1][0]):#same price
                    del bestValue[-1] #remove worse value
                    del bestPrice[-1]
                bestValue.append(item)
                bestPrice.append(item[0])
                continue  
        quantizedValues = [self.quantizer(bestPrice,query) for query in queries] #quantize items to the closest best price
        bestDict = {item[0]: item[1] for item in bestValue}
        beautyBought = []     
        for quantizedValue in quantizedValues:
            beautyBought.append(self.getBeauty(bestDict, quantizedValue)) #get the corresponding beuauty for best prices
        return beautyBought
      

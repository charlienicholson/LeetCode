class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
                return 0
        minprice = max(prices)
        profit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            if(price - minprice) > profit:
                profit = price - minprice
        return profit

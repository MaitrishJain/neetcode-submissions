class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        result = 0 
        while sell < len(prices):
            res = prices[sell]-prices[buy]
            if  res< 0:
                buy = int(sell)
            else:
                result = max(result, res)
                sell += 1
        return result
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        result = 0 
        while sell < len(prices):
            if prices[sell]-prices[buy] < 0:
                buy = int(sell)
            else:
                result = max(result, prices[sell]-prices[buy])
                sell += 1
        return result
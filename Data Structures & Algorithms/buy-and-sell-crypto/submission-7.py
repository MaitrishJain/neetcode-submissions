class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = 0
        # sell = 1
        # result = 0 
        # while sell < len(prices):
        #     res = prices[sell]-prices[buy]
        #     if res < 0:
        #         buy = int(sell)
        #     else:
        #         result = max(result, res)
        #         sell += 1
        # return result
        result = 0
        min_till_now = prices[0]
        for i in range(len(prices)):
            result = max(result, prices[i] - min_till_now)
            min_till_now = min(prices[i], min_till_now)
        return result
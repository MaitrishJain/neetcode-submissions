class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_till_now = prices[0]
        for i in range(len(prices)):
            result = max(result, prices[i] - min_till_now)
            min_till_now = min(prices[i], min_till_now)
        return result
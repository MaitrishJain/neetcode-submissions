class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # result = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         result = max(prices[j]-prices[i], result)
        # return result
        result = 0
        prefix_min_list = [int()]*len(prices)
        prefix_min = prices[0]
        suffix_max_list = [int()]*len(prices)
        suffix_max = prices[-1]
        for i in range(len(prices)):
            if prices[i]<=prefix_min:
                prefix_min = prices[i]
            prefix_min_list[i] = prefix_min
        for j in range(len(prices)):
            if prices[-j-1]>=suffix_max:
                suffix_max = prices[-j-1]
            suffix_max_list[-j-1] = suffix_max
        for k in range(len(prices)):
            result = max(result, suffix_max_list[k]-prefix_min_list[k])
        return result
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # result = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         result = max(prices[j]-prices[i], result)
        # return result
        result = 0
        prefix_min = max(prices)
        prefix_index = 0
        suffix_max = min(prices)
        suffix_index = len(prices) - 1
        for i in range(len(prices)):
            if prices[i] < prefix_min:
                prefix_min = prices[i]
                prefix_index = int(i)
        print(prefix_index)
        while suffix_index!=prefix_index:
            print(suffix_index)
            if prices[suffix_index] > suffix_max:
                suffix_max = prices[suffix_index]
            suffix_index-=1
        print(prefix_min, suffix_max)
        return suffix_max - prefix_min
        

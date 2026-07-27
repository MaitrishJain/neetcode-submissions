from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_list = [0] * (len(nums) + 1)
        counter = defaultdict(int)
        result = []
        for num in nums:
            counter[num] += 1
        for num, freq in counter.items():
            frequency_list[freq] = num
        for i in range(len(nums)):
            if frequency_list[-i]==0:
                continue
            result.append(frequency_list[-i])
            if len(result)==k:
                return result


from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_list = [[] for x in range(len(nums) + 1)]

        counter = defaultdict(int)
        result = []
        for num in nums:
            counter[num] += 1
        for num, freq in counter.items():
            frequency_list[freq].append(num)
        for i in range(len(frequency_list)):
            if not frequency_list[-i]:
                continue
            for j in range(len(frequency_list[-i])):
                result.append(frequency_list[-i][j])
            if len(result)==k:
                break
        return result


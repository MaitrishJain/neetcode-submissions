from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        frequency_map = Counter(nums)
        print(frequency_map)   
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = dict()
        for i in range(len(nums)):
            num_map[nums[i]] = i
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in num_map and num_map[comp] != i:
                return [i, num_map[comp]]


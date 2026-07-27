class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = dict()
        for i in range(len(nums)):
            if nums[i] not in num_map:
                num_map[nums[i]] = i
        for j in num_map.keys():
            comp = target - j
            if comp in num_map:
                return [num_map[j], num_map[comp]]

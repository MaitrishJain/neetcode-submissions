class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        working_result = 1
        result = [1] * len(nums)
        for i in nums:
            print(working_result, i)
            working_result = working_result * i
        print(working_result)
        for i in range(len(nums)):
            result[i] = int(working_result) / nums[i]
        return result
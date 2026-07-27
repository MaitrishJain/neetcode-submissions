class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        working_result = 1
        result = [1] * len(nums)
        for i in nums:
            if i == 0:
                continue
            working_result = working_result * i

        print(working_result)
        for i in range(len(nums)):
            if nums[i] == 0:
                working_result = 0
                continue
            result[i] = int(int(working_result) / nums[i])
        return result
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []*len(nums)
        result = []
        for i in range(1, len(nums)):
            mul = 1
            prefix.append([mul * i for i in nums[:i]][0])
        print(prefix)
        for i in range(-len(nums), -1, -1):
            mul = 1
            suffix[i] = [mul * i for i in nums[i:]][0]
        print(suffix)

        for i in range(len(prefix)):
            result[i] = prefix[i] * suffix[i]
        return result



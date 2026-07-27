class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [] * (len(nums) +1)
        suffix = [] * (len(nums) +1) 
        for i in range(len(nums)):
            mul = 1
            for j in range(i, len(nums)):
                mul *= nums[j]
            suffix[i] = mul
        for i in range(-1, -len(nums)-1, -1):
            mul = 1
            for j in range(i, -len(nums)-1, -1):
                mul *= nums[j]
            prefix[i] = mul
        print(prefix)
        print(suffix)
       


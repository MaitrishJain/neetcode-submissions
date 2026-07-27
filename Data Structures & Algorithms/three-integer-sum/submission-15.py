class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        i = 0
        j = -1
        print(nums)
        while i != len(nums) and j != -len(nums) and len(nums) + j != i + 1:
            print(i, j)
            print(nums[i], nums[j])
            if -(nums[i] + nums[j]) in set(nums[i:j]):
                res = [nums[i], nums[j], -(nums[i] + nums[j])]
                if res not in result:
                    result.append([nums[i], nums[j], -(nums[i] + nums[j])])
            if nums[i] + nums[j] > 0:
                j -= 1
            else:
                i += 1

        return result

        
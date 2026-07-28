from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        start = 0
        end = -1
        frequency_map = Counter(nums)
        nums.sort()
        results = []
        print(frequency_map)
        print(nums)
        while len(nums) + end > start:
            frequency_map[nums[start]] -= 1
            frequency_map[nums[end]] -= 1
            counter = -(nums[start] + nums[end])
            if counter in frequency_map and frequency_map[counter] != 0 and sorted([nums[start], nums[end], counter]) not in results:
                results.append(sorted([nums[start], nums[end], counter]))
            frequency_map[nums[start]] += 1
            frequency_map[nums[end]] += 1
            if nums[start] + nums[end] < 0:
                start += 1
            else:
                end -= 1     
        return results      
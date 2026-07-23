class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hash = set(nums)
        res = 0
        current = 0
        for i in nums:
            if i-1 in nums_hash:
                continue
            cursor = int(i)
            current = 1
            while cursor+1 in nums_hash:
                current += 1
                cursor += 1
            res = max(res, current)
            current = 0
        return res
            
            

            
            
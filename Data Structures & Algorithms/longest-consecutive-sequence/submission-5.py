class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hash = set(nums)
        res = 0 if nums else 0
        current = 1 if nums else 0
        for i in nums:
            current = 0
            if i-1 in nums_hash:
                continue
            cursor = int(i)
            while cursor+1 in nums_hash:
                current += 1
                cursor += 1
            res = max(res, current)
        return res
            
            

            
            
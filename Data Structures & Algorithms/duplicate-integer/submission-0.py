class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map = set()
        for i in nums:
            if i in num_map:
                return True
            num_map.add(i)
        return False
            
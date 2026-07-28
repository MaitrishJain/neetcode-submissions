class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = int()
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                mul = min(heights[i], heights[j]) * (j-i)
                result = max(mul, result)
        return result

        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        result = int()
        while start < end:
            mul = min(heights[start], heights[end]) * (end - start)
            result = max(mul, result)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return result



        
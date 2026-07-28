class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = 1
        result = 0
        current_mul = 1
        start_max = 0
        end_max = 0
        inter_block = 0
        while start < len(height) and end < len(height):
            while height[start] == 0:
                start += 1
            while height[end] == 0:
                end += 1
            if start == end:
                end += 1 
                continue
            start_max = height[start]
            while end < len(height) and height[end] < height[start]:
                inter_block += height[end]
                end += 1
            if end == len(height):
                break
            mul = min(height[start], height[start]) * (end - start - 1) 
            mul -= inter_block
            result += mul
            print(start, end, result, mul)
            inter_block = 0
            mul = 0
            start = end
        return result
            
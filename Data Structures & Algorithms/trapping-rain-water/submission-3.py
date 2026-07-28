class Solution:
    def trap(self, height: List[int]) -> int:
        start = height[0]
        end = height[-1]
        result = 0
        prefix_maxima = []
        suffix_maxima = [0 for x in height]
        for i in range(len(height)):
            start = max(start, height[i])
            prefix_maxima.append(start)
            end = max(end, height[-i-1])
            suffix_maxima[-i-1] = end
        for i in range(len(height)):
            result += min(prefix_maxima[i], suffix_maxima[i]) - height[i]
        return result
        print(prefix_maxima)
        print(suffix_maxima)

            
            
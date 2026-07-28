class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # result = int()
        # for i in range(len(heights)):
        #     for j in range(i, len(heights)):
        #         mul = min(heights[i], heights[j]) * (j-i)
        #         result = max(mul, result)
        # return result
        # indexed_list = list(enumerate(heights))
        # sorted_pairs = sorted(indexed_list, key= lambda x: x[1])

        # indexes = [x for x, y in sorted_pairs]
        # sorted_list = [y for x, y in sorted_pairs]
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



        
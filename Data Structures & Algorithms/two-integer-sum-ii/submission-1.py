class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if i != 0 and numbers[i-1] == numbers[i]:
                return [i, i+1]
            else:
                numbers[i] = target - numbers[i]
        return numbers
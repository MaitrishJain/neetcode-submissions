class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        for i in range(len(s)):
            while not s[start].lower().isalnum() and start < len(s) - 1:
                start += 1
            while not s[end].lower().isalnum() and end < 0:
                end -= 1
            if start > end:
                return True
            if s[start].lower() != s[end].lower():
                return False
            start += 1 
            end -= 1
        return True
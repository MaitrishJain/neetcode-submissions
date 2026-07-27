class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            return "##".join(strs)
        else:
            return ""


    def decode(self, s: str) -> List[str]:
        result = s.split("##")
        return result

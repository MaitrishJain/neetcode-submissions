class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs!=[]:
            return "##".join(strs)
        else:
            return ""


    def decode(self, s: str) -> List[str]:
        print(s)
        result = s.split("##") if s else []
        return result

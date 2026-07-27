class Solution:

    def encode(self, strs: List[str]) -> str:
        return "##".join(strs)


    def decode(self, s: str) -> List[str]:
        print(s)
        result = s.split("##") if s else []
        return result

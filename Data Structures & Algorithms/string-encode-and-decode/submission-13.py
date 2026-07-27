class Solution:

    def encode(self, strs: List[str]) -> str:
        return "##".join(strs) if strs != [] else "null"

    def decode(self, s: str) -> List[str]:
        result = s.split("##") if s is not "null" else []
        return result

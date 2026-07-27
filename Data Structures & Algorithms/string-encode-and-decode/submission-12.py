class Solution:

    def encode(self, strs: List[str]) -> str:
        return "##".join(strs) if strs != [] else None

    def decode(self, s: str) -> List[str]:
        result = s.split("##") if s is not None else []
        return result

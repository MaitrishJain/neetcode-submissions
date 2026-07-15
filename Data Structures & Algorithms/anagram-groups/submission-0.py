from collections import defaultdict
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        str_map = defaultdict(list)
        for i in strs:
            str_map["".join(sorted(i))].append(i)
        return [x for x in str_map.values()]
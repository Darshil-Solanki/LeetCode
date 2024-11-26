class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            map = {}
            for st in strs:
                curSet = "".join(sorted(st))
                if curSet in map:
                    map[curSet].append(st)
                else:
                    map[curSet]=[st]
            return map.values()

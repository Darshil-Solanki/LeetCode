class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        max_num = max(groups)
        mp = defaultdict(int)
        for i, e in enumerate(elements):
            num = e
            if e not in mp:
                while e<=max_num:
                    if e not in mp:
                        mp[e] = i
                    e += num
        result = [ (-1 if g not in mp else mp[g]) for g in groups ]
        return result

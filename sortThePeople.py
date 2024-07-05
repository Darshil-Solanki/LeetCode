class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = list(zip(names,heights))
        res.sort(reverse=True, key=lambda x: x[1])
        return [p[0] for p in res]
        

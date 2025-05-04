class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        ans = 0

        for a, b in dominoes:
            a, b = min(a, b), max(a, b)
            ans += count[(a,b)]
            count[(a,b)] += 1
        
        return ans

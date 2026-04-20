class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        color_idx = defaultdict(list)
        for i, c in enumerate(colors):
            color_idx[c].append(i)
        
        ans = 0
        for c1, indices1 in color_idx.items():
            for c2, indices2 in color_idx.items():
                if c1!=c2:
                    ans = max(ans, abs(indices1[0]-indices2[-1]), abs(indices1[-1]-indices2[0]))
        
        return ans

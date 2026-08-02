class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        cnt = Counter(planks)
        plank_set = list(cnt.keys())
        pair_cnt = defaultdict(int)

        n = len(plank_set)
        for i in range(n):
            p1 = plank_set[i]
            pair_cnt[p1 * 2] += cnt[p1] // 2
            for j in range(i+1, n):
                p2 = plank_set[j]
                pair_cnt[p1 + p2] += min(cnt[p1], cnt[p2])
        
        max_width = 0
        candidate = set(pair_cnt.keys()).union(cnt.keys())
        for height in candidate:
            width = cnt[height] + pair_cnt[height]
            max_width = max(max_width, width)
        
        return max_width

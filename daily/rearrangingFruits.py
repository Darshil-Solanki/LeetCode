class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = Counter(basket1)
        for b2 in basket2:
            cnt[b2] -= 1
        m = min(cnt.keys())

        merge = []
        for key, count in cnt.items():
            if count%2:
                return -1
            merge.extend([key]*(abs(count)//2))

        if not merge:
            return 0

        merge.sort()
        return sum(min(2*m, x) for x in merge[:len(merge)//2])

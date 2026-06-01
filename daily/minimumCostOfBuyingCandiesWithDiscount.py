class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        ans = 0
        for i, c in enumerate(cost):
            if (i+1)%3==0:
                continue
            ans += c
        return ans

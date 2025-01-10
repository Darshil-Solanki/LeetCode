class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<3: return min(cost)
        first, second = cost[0], cost[1]
        for i in range(2, len(cost)):
            first, second = second, cost[i]+min(first,second)
        return min(first, second)

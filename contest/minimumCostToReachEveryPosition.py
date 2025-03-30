class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        mincost = cost[0]
        result = [mincost]

        for i in range(1, len(cost)):
            if cost[i]<mincost:
                mincost = cost[i]
            result.append(mincost)

        return result

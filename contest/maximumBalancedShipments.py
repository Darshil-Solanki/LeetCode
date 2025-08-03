class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        ans = 0
        prev_max = weight[0]
        for i in range(1, len(weight)):
            if weight[i]>=prev_max:
                prev_max = weight[i]
            else:
                ans += 1
                prev_max = weight[i+1] if i<len(weight)-1 else float("inf")
        return ans

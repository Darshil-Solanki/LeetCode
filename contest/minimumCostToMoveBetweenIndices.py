class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        prefix_cost, suffix_cost = [0, 1], [0, 1]
        for i in range(2, len(nums)):
            cost  = 1 if abs(nums[i-1]-nums[i])<abs(nums[i-1]-nums[i-2]) else abs(nums[i-1]-nums[i])
            prefix_cost.append(prefix_cost[-1]+cost)
        for i in range(len(nums)-3, -1, -1):
            cost = 1 if abs(nums[i+1]-nums[i])<=abs(nums[i+1]-nums[i+2]) else abs(nums[i+1]-nums[i])
            suffix_cost.append(suffix_cost[-1]+cost)
        suffix_cost.reverse()
        ans = []
        for l, r in queries:
            if l<r:
                ans.append(prefix_cost[r]-prefix_cost[l])
            else:
                ans.append(suffix_cost[r]-suffix_cost[l])
        return ans

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        adj = [1]
        for i in range(1, len(nums)):
            adj.append(adj[i-1]+1 if nums[i]>nums[i-1] else 1)
            if i>=k:
                if adj[i]>=k and adj[i-k]>=k:
                    return True
        return False
    # Dynamic Programming Bottom Up Approach with space Space Optimization 
    # def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
    #     prev_increase, cur_increase = 0,1
    #     longest_k = 0
    #     for i in range(1, len(nums)):
    #         if nums[i] > nums[i - 1]: cur_increase += 1
    #         else: prev_increase, cur_increase = cur_increase, 1
    #         longest_k = max(longest_k, cur_increase // 2, min(prev_increase, cur_increase))
    #     return longest_k >= k

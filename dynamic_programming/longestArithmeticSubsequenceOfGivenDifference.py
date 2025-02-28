class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        map = {}
        for n in arr:
            if n-difference in map:
                map[n] = 1+map[n-difference]
            else:
                map[n] = 1
        return max(map.values())
        # max_len = 0
        # dp = [1]*len(arr)

        # for i in range(len(arr)-1, -1, -1):
        #     for j in range(i+1, len(arr)):
        #         if arr[j]-arr[i]==difference and dp[j]+1>dp[i]:
        #             dp[i] = dp[j]+1
        
        # return max(dp)

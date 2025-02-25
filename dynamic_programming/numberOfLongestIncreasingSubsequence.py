class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1]*n
        count = [1]*n
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i]<nums[j]:
                    if length[i] < length[j]+1:
                        length[i] = length[j]+1
                        count[i] = count[j]
                    elif length[i] == length[j]+1:
                        count[i] += count[j]
        
        mx_len = max(length)
        ans = 0
        for i, l in enumerate(length):
            if l==mx_len:
                ans += count[i]
        return ans

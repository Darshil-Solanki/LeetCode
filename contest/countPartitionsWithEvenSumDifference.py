class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        temp = 0
        prefixSum = []
        for n in nums:
            temp+=n
            prefixSum.append(temp)
        n = len(nums)-1
        ans = 0
        for i, sm in enumerate(prefixSum):
            if i==n: break
            if abs(prefixSum[n]-prefixSum[i] - prefixSum[i])%2==0:
                ans+=1
        return ans

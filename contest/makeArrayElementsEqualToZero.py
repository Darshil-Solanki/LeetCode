class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        zeroes = []
        count = 0
        n = len(nums)
        if nums[0]==0: zeroes.append(0)
        for i in range(1,n):
            prefixSum.append(prefixSum[i-1]+nums[i])
            if nums[i]==0:
                zeroes.append(i)
        for idx in zeroes:
            left = prefixSum[idx-1] if idx-1>-1 else 0
            right = (prefixSum[n-1]-prefixSum[idx])
            diff = abs(left-right)
            if diff==1:
                count+=1
            elif diff==0:
                count+=2
        return count 

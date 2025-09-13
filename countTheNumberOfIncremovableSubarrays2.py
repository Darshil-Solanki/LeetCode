class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        segments = [[nums[0]]]
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                segments[-1].append(nums[i])
            else:
                segments.append([nums[i]])
        
        n = len(segments)
        if n==1:
            return (len(nums)+1)*(len(nums))//2 # all increasing so ans is (n^2+n)/2
        
        ans = len(segments[0])+len(segments[-1])+1 # left inc. + right inc. + empty array count
        right=0
        for i in range(len(segments[0])):
            while right<len(segments[-1]) and segments[-1][right]<=segments[0][i]:
                right += 1
            
            if right == len(segments[-1]):
                break
            ans += len(segments[-1])-right

        return ans      

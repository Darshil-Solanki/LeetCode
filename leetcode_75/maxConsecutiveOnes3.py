class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, ans, temp = 0, 0, 0
        for right, curr in enumerate(nums):
            if curr: temp += 1
            else:
                nums[right]=-1
                temp+=1
                k-=1    
            while k<0:
                if nums[left]==-1:
                    nums[left] = 0
                    k+=1
                temp-=1
                left+=1
            if temp>ans: ans = temp
        return ans

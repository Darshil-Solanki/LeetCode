class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, ans, temp = 0, 0, 0
        for right, curr in enumerate(nums):
            if curr: temp += 1
            else:
                temp+=1
                k-=1    
            while k<0:
                if not nums[left]:
                    k+=1
                temp-=1
                left+=1
            if temp>ans: ans = temp
        return ans

        # faster version
        # l = r = 0
        # for num in nums:
        #     if num == 0:
        #         k -= 1
        #     if k < 0:
        #         if nums[l] == 0:
        #             k += 1
        #         l += 1
        # return len(nums) - l

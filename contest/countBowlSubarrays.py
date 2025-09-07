class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        ans = 0
        stack = []

        for num in nums:
            while stack and stack[-1]<num:
                stack.pop()
                ans += 1 
            if stack:
                ans += 1
            stack.append(num)

        return ans-(len(nums)-1)

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        i = 0
        while i<n:
            stack.append(nums[i])
            while len(stack)>1 and stack[-1]==stack[-2]:
                stack.pop()
                stack[-1] += stack[-1]
            i += 1
    
        return stack

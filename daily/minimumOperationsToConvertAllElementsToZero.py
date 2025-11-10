class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ops = 0

        for num in nums:
            while stack and stack[-1]>num:
                stack.pop()
            if not num:
                continue
            if not stack or stack[-1]<num:
                ops += 1
                stack.append(num)
        
        return ops

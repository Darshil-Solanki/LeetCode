class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if not n:
            return 0
        mx = curr = 1
        for i in range(1,n):
            if nums[i-1]==nums[i]:
                continue
            if  nums[i-1]+1==nums[i]:
                curr+=1
            else:
                curr=1
            mx = curr if curr>mx else mx
        return mx
		# Better and proper hashmap method
		# s = set(t)
		# q = 0
		# while s:
		#     n = s.pop()
		#     l = n - 1
		#     while l in s:
		#         s.remove(l)
		#         l-=1
		#     h = n + 1
		#     while h in s:
		#         s.remove(h)
		#         h+=1
		#     q = max(q, h-l-1)
		# return q

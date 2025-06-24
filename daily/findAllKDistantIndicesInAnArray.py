class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        added = [False]*n
        result = []

        for i, num in enumerate(nums):
            if num == key:
                for k_idx in range(max(0, i-k), min(i+k+1,n)):
                    if not added[k_idx]:
                        added[k_idx] = True
                        result.append(k_idx)
        
        return result

        # faster approach using last added index instead of tracking all index added 
        # res = []
        # r = 0  # unjudged minimum index
        # n = len(nums)
        # for j in range(n):
        #     if nums[j] == key:
        #         l = max(r, j - k)
        #         r = min(n - 1, j + k) + 1
        #         for i in range(l, r):
        #             res.append(i)
        # return res

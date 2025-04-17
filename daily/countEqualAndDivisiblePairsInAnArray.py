class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        indices = defaultdict(list)
        
        for i, n in enumerate(nums):
            for j in indices[n]:
                if i * j % k == 0:
                    ans += 1

            indices[n].append(i)
        
        return ans

        # brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j] and i*j%k == 0:
        #             ans += 1
        
        # return ans

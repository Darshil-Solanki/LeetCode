class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        hashset = defaultdict(int)
        for n in nums:
            hashset[n] += 1

        ans = float("-inf")
        total = sum(nums)
        for n in nums:
            x = total-n
            targetsum = x//2
            if targetsum in hashset and x-targetsum==targetsum:
                if targetsum==n:
                    if hashset[n]>1:
                        ans = max(ans, n)
                else:
                    ans = max(ans, n)
        
        return ans

        # little bit better with counter to optimize 
        # cnt = Counter(nums)
        # total = sum(nums)
        # max_outlier = -inf
        # for num in cnt:
        #     outlier = total - 2*num
        #     if outlier in cnt:
        #         #check in outlier is num
        #         if outlier == num and cnt[num] == 1:
        #             continue
        #         max_outlier = max(outlier, max_outlier)
        # return max_outlier

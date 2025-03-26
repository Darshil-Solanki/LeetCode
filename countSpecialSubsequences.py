class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        pairs = defaultdict(list)
        n = len(nums)
        for i in range(n):
            for j in range(i+2, n):
                division = nums[i]/nums[j]
                pairs[division].append(j)
        
        for product in pairs:
            pairs[product] = sorted(pairs[product])

        ans = 0
        for i in range(n):
            for j in range(i+2, n):
                division = nums[j]/nums[i]
                indices = pairs[division]
                idx = bisect_right(indices, i-2)
                ans+=idx
        
        return ans

        # from solution O(n**2)
        # ans = 0
        # pairs = defaultdict(float)
        # for q in range(2, len(nums) - 4):
        #     for p in range(q - 1):
        #         pairs[nums[p] / nums[q]] += 1
        #     r = q + 2
        #     for s in range(r + 2, len(nums)):
        #         ans += pairs[nums[s] / nums[r]]
        # return int(ans)

        # brute force tle
        # pairs = defaultdict(list)
        # n = len(nums)
        # for p in range(n):
        #     for r in range(p+2, n):
        #         product = nums[p]*nums[r] 
        #         pairs[product].append((p, r))
        
        # ans = 0
        # for q in range(n):
        #     for s in range(q+2, n):
        #         product = nums[q]*nums[s]
        #         for p, r in pairs[product]:
        #             if q-p>1 and r-q>1 and s-r>1: ans+=1
        
        # return ans

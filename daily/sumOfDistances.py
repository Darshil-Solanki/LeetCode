class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups = defaultdict(list)
        for i, num in enumerate(nums):
            groups[num].append(i)
        
        ans = [0]*len(nums)
        for group in groups.values():
            total = sum(group)
            prefix_total = 0
            m = len(group)
            for i, idx in enumerate(group):
                ans[idx] = total - prefix_total*2 + idx*( 2*i - m) 
                prefix_total += idx
        
        return ans



        # TLE
        # ans = []        
        # for i, num in enumerate(nums):
        #     if len(indices[num])<2:
        #         ans.append(0)
        #         continue
        #     ans.append(sum(abs(i-j) for j in indices[num] if i!=j))

        # return ans

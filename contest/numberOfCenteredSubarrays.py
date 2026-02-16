class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        ans = len(nums)
        prefix_sum, temp = [], 0
        
        for n in nums:
            temp += n
            prefix_sum.append(temp)    

        for i, n in enumerate(nums):
            curr_num = set([n])
            for j in range(i+1, len(nums)):
                curr_num.add(nums[j])
                tot = prefix_sum[j]-(prefix_sum[i-1] if i>0 else 0)
                if tot in curr_num:
                    ans += 1

        return ans

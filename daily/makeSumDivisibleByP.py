class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        ans = len(nums)
        tot = sum(nums)
        if tot%p == 0: return 0
        target = tot%p

        mod_map = {0:-1}
        curr_sum = 0
        for i, n in enumerate(nums):
            curr_sum = (curr_sum+n)%p
            needed = (curr_sum - target + p)%p
            
            if needed in mod_map:
                ans = min(ans, i-mod_map[needed])
            
            mod_map[curr_sum] = i
        
        return -1 if ans==len(nums) else ans

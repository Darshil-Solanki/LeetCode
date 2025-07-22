class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        u_set = set()
        left = ans = tot = 0

        for right, num in enumerate(nums):
            while num in u_set:
                u_set.remove(nums[left])
                tot -= nums[left]
                left += 1
            
            u_set.add(num)
            tot += num
            ans = max(ans, tot)
        
        return ans

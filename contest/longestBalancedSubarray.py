class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        for l in range(n):
            odd_set, even_set = {},{}
            if nums[l]%2:
                odd_set[nums[l]] = True
            else:
                even_set[nums[l]] = True
            for r in range(l+1, n):
                if nums[r]%2 and nums[r] not in odd_set:
                    odd_set[nums[r]] = True
                    
                if not nums[r]%2 and nums[r] not in even_set:
                    even_set[nums[r]] = True
                
                if len(odd_set) == len(even_set):
                    ans = max(ans, r-l+1)

        return ans

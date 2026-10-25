class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        curr_length = 0
        ans = 0
        
        for num in nums:
            if num<minK or num>maxK:
                curr_length = 0
                continue

            curr_length += 1
            ans += curr_length

        return ans

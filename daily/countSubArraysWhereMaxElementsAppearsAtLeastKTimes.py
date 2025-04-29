class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        left = ans = count = 0
        n = len(nums)

        for right, num in enumerate(nums):
            if num == max_element:
                count+=1

            while count>=k:
                ans += n-right
                if nums[left]==max_element:
                    count -= 1
                left += 1
            
        return ans

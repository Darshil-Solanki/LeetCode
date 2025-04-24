class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distincts = len(set(nums))
        count_map = defaultdict(int)
        
        ans = left = 0
        for right, num in enumerate(nums):
            count_map[num] += 1

            while len(count_map)==distincts:
                ans += n-right
                count_map[nums[left]] -= 1
                if not count_map[nums[left]]:
                    del count_map[nums[left]]
                left += 1
        
        return ans

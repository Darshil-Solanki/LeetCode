class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        ans = 0
        cnt = Counter()
        modes = set()

        def add_mode(value):
            modes.add(value)
            if value-k >= nums[0]:
                modes.add(value - k)
            if value+k <= nums[-1]:
                modes.add(value + k)
            
        prev_index = 0
        for i, n in enumerate(nums):
            if n != nums[prev_index]:
                cnt[nums[prev_index]] = i - prev_index 

                ans = max(ans, i-prev_index)
                add_mode(nums[prev_index])
                prev_index = i
        
        cnt[nums[prev_index]] = len(nums) - prev_index
        ans = max(ans, len(nums)-prev_index)
        add_mode(nums[prev_index])

        for mode in sorted(modes):
            l = bisect_left(nums, mode-k)
            r = bisect_right(nums, mode+k)-1
            if mode in cnt:
                temp = min(r-l+1, cnt[mode]+numOperations)
            else:
                temp = min(r-l+1, numOperations)
            ans = max(ans, temp)
        
        return ans

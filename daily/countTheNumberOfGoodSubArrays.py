class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = ans = 0
        count = {}
        same = 0
        
        for n in nums:
            same += count.get(n, 0)
            count[n] = count.get(n, 0) + 1

            while same>=k:
                count[nums[left]] -= 1
                same -= count[nums[left]]
                left += 1

            ans += left
        
        return ans

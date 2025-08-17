class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        arr = sorted(abs(x) for x in nums)
        n = len(arr)
        left = ans = 0

        for right in range(n):
            while left<right and arr[right]>2*arr[left]:
                left += 1
            
            ans += right-left
        
        return ans

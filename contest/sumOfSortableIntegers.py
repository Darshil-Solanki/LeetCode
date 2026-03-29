class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        if nums==sorted(nums):
            return sum(i for i in range(1, n+1) if n%i==0)

        def check(k):
            prev_max = float("-inf")
            for start in range(0, n-k+1, k):
                part = nums[start:start+k]
                mn, mx = min(part), max(part)
                if part==sorted(part):
                    if mn<prev_max:
                        return False
                    prev_max = mx
                    continue
                temp = 0
                for i in range(start, start+k-1):
                    if nums[i]>nums[i+1]:
                        temp += 1
                if temp < 2:
                    if nums[start+k-1]>nums[start]:
                        return False
                if temp>1:
                    return False
                if mn<prev_max:
                    return False
                prev_max = mx
                
            return True

        return sum(i for i in range(2, n+1) if n%i==0 and check(i))

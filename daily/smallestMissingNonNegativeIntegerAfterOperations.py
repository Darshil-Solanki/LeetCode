class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        rem = [0]*value
        for n in nums:
            rem[n%value] += 1

        for i in range(len(nums)):
            t = i%value
            if rem[t]:
                rem[t] -= 1
                continue
            return i
            
        return len(nums)

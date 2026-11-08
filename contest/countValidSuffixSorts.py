class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        n = len(nums)
        unmatching = 0
        prefix_match = [True] * (n+1)
        diff = {}

        for i in range(n):
            prefix_match[i+1] = prefix_match[i] and nums[i] == target[i]

        def update(x, delta):
            nonlocal unmatching
            old = diff.get(x, 0)
            new = old + delta

            if old == 0 and new != 0:
                unmatching += 1
            elif old !=0 and new == 0:
                unmatching -= 1

            if new:
                diff[x] = new
            else:
                diff.pop(x, None)
            
        ans = 0
        for i in range(n-1, -1, -1):
            update(nums[i], 1)
            update(target[i], -1)
            
            if i<n-1 and target[i] < target[i+1]:
                break
                
            ans += prefix_match[i] and unmatching == 0

        return ans

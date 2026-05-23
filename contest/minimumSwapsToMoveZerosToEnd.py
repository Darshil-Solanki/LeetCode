class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        last_z = n-1
        
        for i in range(n):
            if nums[i]==0 and i<last_z:
                while last_z>i and nums[last_z]==0:
                    last_z -= 1
                if i>=last_z:
                    return ans
                nums[last_z] = 0
                last_z -= 1
                ans += 1

        return ans

        # simplify above logic (code from contest ranking)
        # c = a.count(0)
        # a.reverse()
        # ans = 0
        # for i in range(c):
        #     ans += a[i] != 0
        # return ans

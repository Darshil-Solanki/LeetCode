class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = True
        prev = nums[0]
        max_n = float("inf")
        for n in nums:
            if prev<=n<=max_n:
                pass
            else:
                if flag:
                    if n>nums[0]: return False
                    max_n = nums[0]
                    flag = False
                else:
                    return False
            prev = n
        return True

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def check(k):
            for i in range(len(nums)-k+1):
                bitMask = 0
                is_nice = True

                for j in range(i, i+k):
                    if bitMask & nums[j]:
                        is_nice = False
                        break
                    bitMask |= nums[j]

                if is_nice:
                    return True
            return False

        left, right = 1, 30

        while left<=right:
            mid = (left+right)//2
            if check(mid):
                left = mid+1
            else:
                right = mid-1
        
        return right

        # sliding window technique reverse check
        # ans = 1
        # for i, orv in enumerate(nums):
        #     j = i - 1
        #     while j >= 0 and (orv & nums[j] == 0):
        #         orv |= nums[j]
        #         j -= 1
        #     ans = max(ans, i - j)
        # return ans

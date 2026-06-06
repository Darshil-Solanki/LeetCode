class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left, right = 0, sum(nums)
        ans = []
        for n in nums:
            right -= n
            ans.append(abs(left-right))
            left += n
        return ans

        # left, right = [], []
        # temp = 0
        # for n in nums:
        #     left.append(temp)
        #     temp += n
        # for n in nums:
        #     temp -= n
        #     right.append(temp)
        
        # return [abs(a-b) for a, b in zip(left, right)]

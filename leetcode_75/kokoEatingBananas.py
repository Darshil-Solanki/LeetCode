class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def check(k):
            return sum((pile + k - 1) // k for pile in piles) <= h
        left, right = 1, max(piles)
        while left<=right:
            mid = (left+right)//2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

        # fastest method
        # n = len(piles)
        # s = sum(piles)
        # l = math.ceil(s/h)
        # r =  math.ceil(s/(h - n + 1))
        # while l < r:
        #     m = (l + r) //2
        #     hours = 0
        #     for i in piles:
        #         hours += math.ceil(i/m)
        #     if hours<=h:
        #         r = m
        #     else:
        #         l = m + 1
        # return l

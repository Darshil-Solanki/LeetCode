class Solution:
    def minimumK(self, nums: List[int]) -> int:
        def check(k):
            op = 0
            for num in nums:
                op += num//k
                if num%k:
                    op+=1

            return op<=k*k

        left, right = 1, max(max(nums),len(nums))
        ans = right
        while left<=right:
            mid = (left+right)//2
            if check(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1

        return anss

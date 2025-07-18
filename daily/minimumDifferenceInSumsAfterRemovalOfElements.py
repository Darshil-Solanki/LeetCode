class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n3, n = len(nums), len(nums)//3
        
        left = [0]*(n+1)
        left_total = sum(nums[:n])
        # max_heap
        left_max_heap = [-x for x in nums[:n]]
        heapify(left_max_heap)
        left[0] = left_total

        for i in range(n, 2*n):
            left_total += nums[i]
            left_total -= -heappushpop(left_max_heap, -nums[i])
            left[i-(n-1)] = left_total
        
        right_total = sum(nums[2*n:])
        right_min_heap = nums[2*n:]
        heapify(right_min_heap)
        ans = left[n] - right_total
        
        for i in range(2*n-1, n-1, -1):
            right_total += nums[i]
            right_total -= heappushpop(right_min_heap, nums[i])
            ans = min(ans, left[i-n]-right_total)

        return ans

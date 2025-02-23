class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(limits)
        heap = []
        for i in range(n):
            if not limits[i]: continue
            grid[i].sort()
            nums = grid[i][-limits[i]:]
            for n in nums:
                heap.append(-n)
        heapify(heap)
        ans = 0
        for i in range(k):
            ans+=(-heappop(heap))
        return ans

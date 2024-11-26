class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap,(n,n))
            while len(heap)>k:
                heapq.heappop(heap)
        return heap[0][0]

        # heap = nums[:k]
        # heapq.heapify(heap)

        # for num in nums[k:]:
        #     heapq.heappush(heap, num)
        #     heapq.heappop(heap)
        
        # return heap[0]

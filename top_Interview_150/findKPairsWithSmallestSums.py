class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []   # min heap
        for i in range(min(len(nums1), k)):
            heapq.heappush(heap, (nums1[i]+nums2[0], 0)) # pushing sum as criteria and pos as value
        pair = []
        while k>0:
            s, pos = heapq.heappop(heap)    # sum and position of num2 element
            pair.append([s-nums2[pos], nums2[pos]])
            if pos+1<len(nums2):    # if there exist more nums2 element add them to min heap
                heapq.heappush(heap, (s-nums2[pos]+nums2[pos+1], pos+1))
            k-=1
        return pair

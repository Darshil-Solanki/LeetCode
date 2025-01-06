class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        #Neetcode Youtube Solution
        pairs = list(zip(nums1, nums2))
        pairs.sort(key=lambda ab: -ab[1])
        
        ans = tot = 0
        mulHeap = []
        for a, b in pairs:
            tot+=a
            heappush(mulHeap, a)
            if len(mulHeap)>k:
                tot -= heappop(mulHeap)
            if len(mulHeap)==k:
                ans = max(ans, tot*b)
        return ans

        # copied from submission
        # arr = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        # h = [x for x, _ in arr[:k]]
        # heapify(h)

        # tot = sum(h)
        # ans = tot * arr[k - 1][1]

        # for n1, n2 in arr[k:]:
        #     if n1 > h[0]:
        #         tot += n1 - heapreplace(h, n1)
        #         ans = max(ans, tot * n2)
                
        # return ans

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0
        
        diff.sort(reverse = True)
        diff.append(0)

        for i in range(1, len(nums1)+1):
            cost = (diff[i-1] - diff[i]) * i
            if cost > k:
                q, r = divmod(k, i)
                hi = diff[i-1] - q
                return (
                    hi * hi * (i-r) +
                    (hi - 1) * (hi - 1) * r +
                    sum(x * x for x in diff[i:])
                )
            k -= cost
        
        return 0          

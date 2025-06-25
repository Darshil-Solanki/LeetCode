class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_product(m1, value):
            if m1>0:
                return bisect_right(nums2, value//m1)
            elif m1<0:
                return len(nums2) - bisect_left(nums2, -(-value//m1))
            else:
                return len(nums2) if value>=0 else 0

        len1 = len(nums1)
        left, right = -10_000_000_000, 10_000_000_000
        
        while left<=right:
            mid = (left+right)//2
            count = 0

            for i, num1 in enumerate(nums1):
                count += count_product(num1, mid)
            
            if count<k:
                left = mid+1
            else:
                right = mid-1
        
        return left

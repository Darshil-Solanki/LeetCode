class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        if nums1==nums2:
            return 0

        def find(nums, split):
            if nums==nums2:
                return True
            if not split:
                return False
                
            for l in range(n):
                left = nums[:l+1]
                for r in range(l+1, n):
                    new = left+nums[r+1:]
                    mid = nums[l+1:r+1]
                    for i in range(len(new)):
                        if find(new[:i]+mid+new[i:], split-1):
                            return True
            return False
                    
        def check(split):
            return find(nums1[:], split)
            
        for i in range(1, n+1):
            if check(i):
                return i
        return n

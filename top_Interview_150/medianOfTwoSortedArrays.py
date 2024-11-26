class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        smallArr, bigArr = nums1, nums2
        if len(nums1)>len(nums2):
            smallArr, bigArr = bigArr, smallArr
        m, n = len(smallArr), len(bigArr)
        total, half = m+n, (m+n)//2
        l, r = 0, m-1
        while True:
            smallMid = (l+r)//2
            bigMid = half - smallMid - 2
            smallLeft = smallArr[smallMid] if smallMid>-1 else float('-inf')
            smallRight = smallArr[smallMid+1] if smallMid+1<m else float('inf')
            bigLeft = bigArr[bigMid] if bigMid>-1 else float('-inf')
            bigRight = bigArr[bigMid+1] if bigMid+1<n else float('inf')
            
            if smallLeft<=bigRight and bigLeft<=smallRight:
                if (m+n)%2:
                    return min(smallRight, bigRight)
                else:
                    return (min(smallRight, bigRight)+max(smallLeft, bigLeft))/2
            elif smallLeft<=bigRight:
                l = smallMid+1
            else:
                r = smallMid-1

        # Two Pointer Method
        # m, n = len(nums1), len(nums2)
        # i, j, m1, m2 = 0, 0, 0, 0
        # for _ in range(((m+n)//2)+1):
        #     m1 = m2
        #     if i<m  and j<n:
        #         if nums1[i] < nums2[j]:
        #             m2 = nums1[i]
        #             i+=1
        #         else:
        #             m2 = nums2[j]
        #             j+=1
        #     elif i<m:
        #         m2 = nums1[i]
        #         i+=1
        #     else:
        #         m2 = nums2[j]
        #         j+=1
        # return  m2 if (m+n)%2 else (m1+m2)/2

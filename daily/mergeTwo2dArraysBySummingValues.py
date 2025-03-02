class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        map = defaultdict(int)
        for id, val in nums1:
            map[id] = val
        
        for id, val in nums2:
            map[id]+=val
        
        ans = []
        for id, val in sorted(map.items()):
            ans.append([id,val])
        
        return ans

        # Two Pointer Faster method
        # left =0
        # right=0
        # ans =[]

        # while left<len(nums1) and right<len(nums2):
        #     if nums1[left][0] == nums2[right][0]:
        #         ans.append([nums1[left][0], nums1[left][1] + nums2[right][1]])
        #         left+=1
        #         right+=1
        #     elif nums1[left][0] < nums2[right][0]:
        #         ans.append(nums1[left])
        #         left+=1
        #     else:
        #         ans.append(nums2[right])
        #         right+=1 

        # while left<len(nums1):
        #         ans.append(nums1[left])
        #         left+=1

        # while right<len(nums2):
        #         ans.append(nums2[right])
        #         right+=1

        # return 

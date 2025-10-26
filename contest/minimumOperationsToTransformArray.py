class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        last = nums2[-1]
        curr, curr_diff = 0, float("inf")
        ans = 0
        for i in range(len(nums1)):
            if abs(nums1[i] - last)<curr_diff:
                curr = nums1[i]
                curr_diff = abs(nums1[i] - last)
            if nums1[i] == last or nums2[i] == last or nums1[i]<last<nums2[i] or nums1[i]>last>nums2[i]:
                nums1.append(last)
                break
            if abs(nums2[i] - last)<curr_diff:
                curr = nums2[i]
                curr_diff = abs(nums2[i]-last)
        else:
            nums1.append(curr)
        ans += 1
        
        for n1, n2 in zip(nums1, nums2):
            ans += abs(n1-n2)
        
        return ans

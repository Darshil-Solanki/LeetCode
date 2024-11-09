class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeftHeight = []
        maxH = -1
        for h in height:
            maxH = h if h>maxH else maxH
            maxLeftHeight.append(maxH)
        maxH = -1
        maxRightHeight = []
        for i in range(len(height)-1, -1, -1):
            maxH = height[i] if height[i]>maxH else maxH
            maxRightHeight.insert(0, maxH)
        amount = 0
        for i in range(1,len(height)-1):
            amount+=min(maxLeftHeight[i],maxRightHeight[i])-height[i]
        return amount

    # Binary Search Version reducing complexity to O(logn) from O(3n)
    # def trap(self, height: List[int]) -> int:
    #     left, right = 0, len(height) - 1
    #     maxleft, maxright = 0, 0
    #     ans = 0

    #     while left < right:
    #         if height[left] < height[right]:
    #             if height[left] > maxleft:
    #                 maxleft = height[left]
    #             else:
    #                 ans += (maxleft - height[left])
    #             left += 1
    #         else:
    #             if height[right] > maxright:
    #                 maxright = height[right]
    #             else:
    #                 ans += (maxright - height[right])
    #             right -= 1
        
    #     return ans

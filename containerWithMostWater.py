class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=mx=0
        r=len(height)-1
        while l<r:
            cur=(r-l)*min(height[l],height[r])
            mx = cur if cur>mx else mx
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return mx

class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        if k>n*(n+1)/2: return -1
        self.count = 0

        def binary_search(nums, target):
            left, right = 0, len(nums)
            while left<=right:
                mid = (left+right)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    left = mid+1
                else:
                    right = mid-1
            return -1
        
        star = []
        def calculate_valid(i):
            bisect.insort(star, i)
            pos = binary_search(star, i)
            left = i if pos==0 else i-1-star[pos-1]
            right =  n-i-1 if pos==len(star)-1 else star[pos+1]-i-1
            self.count += left+1+right+left*right
            return self.count>=k
            
        for time, i in enumerate(order):
            if calculate_valid(i):
                return time
        
        return -1

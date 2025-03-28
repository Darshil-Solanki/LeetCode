class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(w)
        self.frequency = [ weight/self.total for weight in w]
        for i in range(1, len(self.frequency)):
            self.frequency[i]+=self.frequency[i-1] 

    def pickIndex(self) -> int:
        random_idx = random.random()
        left, right = 0, len(self.frequency)-1

        while left<right:
            mid = (left+right)//2
            if random_idx<=self.frequency[mid]:
                right = mid
            else:
                left = mid+1
        
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

class SegmentTree:
    def __init__(self, baskets):
        self.n = len(baskets)
        size = 2<<(self.n-1).bit_length()
        self.tree = [0]*size
        self._build(baskets, 1, 0, self.n-1)
    
    def _maintain(self, i):
        self.tree[i] = max(self.tree[i*2], self.tree[i*2+1])
    
    def _build(self, arr, i, left, right):
        if left==right:
            self.tree[i] = arr[left]
            return 
        
        mid = (left+right)//2
        self._build(arr, i*2, left, mid)
        self._build(arr, i*2+1, mid+1, right)
        self._maintain(i)
    
    def find_first_and_update(self, i, left, right, target):
        if self.tree[i]<target:
            return -1
        if left==right:
            self.tree[i] = -1
            return left
        mid = (left+right)//2
        j = self.find_first_and_update(i*2, left, mid, target)
        if j==-1:
            j = self.find_first_and_update(i*2+1, mid+1, right, target)
        self._maintain(i)
        return j

        
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        if not baskets: return n
        tree = SegmentTree(baskets)
        ans = 0

        for fruit in fruits:
            if tree.find_first_and_update(1, 0, n-1, fruit) == -1:
                ans += 1
        
        return ans


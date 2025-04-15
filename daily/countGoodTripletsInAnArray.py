# Binary Indexed Tree(Fenwick Tree)
class BIT:
    def __init__(self, size):
        self.tree = [0]*(size+1)
    
    def update(self, index, delta):
        index+=1
        while index <= len(self.tree)-1:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index):
        index += 1
        ans = 0
        while index > 0:
            ans += self.tree[index]
            index -= index & -index
        return ans

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2, reversedIndexMapping = [0]*n, [0]*n

        for i, num2 in enumerate(nums2):
            pos2[num2] = i
        for i, num1 in enumerate(nums1):
            reversedIndexMapping[pos2[num1]] = i
        
        tree = BIT(n)
        ans = 0

        for value in range(n):
            pos = reversedIndexMapping[value]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (n-1-pos)-(value-left)
            ans += left*right
        
        return ans
        # Copied from editorial still don't understand concept of Binary Indexed Tree

class SegmentTree:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.prefix, self.suffix = [0] * (4 * self.n), [0] * (4 * self.n)
        self.max_length = [0] * (4 * self.n)
        self.left_char, self.right_char = [""] * (4 * self.n), [""] * (4 *self.n)
    
    def build(self, u, l, r):
        if l == r:
            self.prefix[u] = self.suffix[u] = self.max_length[u] = 1
            self.left_char[u] = self.right_char[u] = self.s[l]
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)
        self.push_up(u, l, r)
    
    def push_up(self, u, l, r):
        mid = (l + r) >> 1
        left_len = mid - l + 1
        right_len = r - mid
        left = u << 1
        right = u << 1 | 1
        self.left_char[u] = self.left_char[left]
        self.right_char[u] = self.right_char[right]
        self.prefix[u] = self.prefix[left]
        if self.prefix[left] == left_len and self.right_char[left] == self.left_char[right]:
            self.prefix[u] = self.prefix[left] + self.prefix[right]
        self.suffix[u] = self.suffix[right]
        if self.suffix[right] == right_len and self.right_char[left] == self.left_char[right]:
            self.suffix[u] = self.suffix[right] + self.suffix[left]
        self.max_length[u] =  max(self.max_length[left], self.max_length[right])
        if self.right_char[left] == self.left_char[right]:
            self.max_length[u] = max(self.max_length[u], self.suffix[left]+self.prefix[right])
    
    def update(self, u, l, r, pos, ch):
        if l==r:
            self.left_char[u] =  ch
            self.right_char[u] = ch
            return
        mid = (l + r) >> 1
        if pos <= mid:
            self.update(u << 1, l, mid, pos, ch)
        else:
            self.update(u << 1 | 1, mid + 1, r, pos, ch)
        self.push_up(u, l, r)
    

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        # copied from editorial
        tree = SegmentTree(s)
        n = len(s)
        tree.build(1, 0, n-1)
        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            tree.update(1, 0, n-1, idx, ch)
            ans.append(tree.max_length[1])
        return ans

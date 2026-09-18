class Seg:
    def __init__(self, left=-1, right=-1):
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return (
            self.left > other.left if self.right==other.right else self.right<other.right
        )
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        seg = [Seg() for _ in range(26)]
        for i, c in enumerate(s):
            idx = ord(c) - ord("a")
            if seg[idx].left == -1:
                seg[idx].left = seg[idx].right = i
            else:
                seg[idx].right = i
        
        for i in range(26):
            if seg[i].left != -1:
                j = seg[i].left
                while j <= seg[i].right:
                    char_idx = ord(s[j]) - ord("a")
                    if not(seg[i].left <= seg[char_idx].left and seg[char_idx].right <= seg[i].right):
                        seg[i].left = min(seg[i].left, seg[char_idx].left)
                        seg[i].right = max(seg[i].right, seg[char_idx].right)
                        j = seg[i].left
                    j += 1
        
        seg.sort()

        ans = []
        end = -1
        for segment in seg:
            left, right = segment.left, segment.right
            if left == -1:
                continue
            if end == -1 or left>end:
                end = right
                ans.append(s[left : right+1])
        
        return ans

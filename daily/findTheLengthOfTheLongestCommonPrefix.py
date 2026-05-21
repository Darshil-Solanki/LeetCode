class TrieNode:
    def __init__(self):
        self.children = [None]*10

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.seen = set()
    
    def insert(self, num):
        if num in self.seen:
            return
        self.seen.add(num)
        node = self.root
        num_str = str(num)
        for digit in num_str:
            idx = int(digit)
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
    
    def find_prefix(self, num):
        node = self.root
        num_str = str(num)
        n = 0

        for digit in num_str:
            idx = int(digit)
            if not node.children[idx]:
                return n
            n += 1
            node = node.children[idx]
        
        return n


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        tree = Trie()
        for num in arr1:
            tree.insert(num)
        
        ans = 0
        for num in arr2:
            ans = max(ans, tree.find_prefix(num))
        
        return ans

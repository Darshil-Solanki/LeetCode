class TrieNode:
    def __init__(self):
        self.children = {}
        self.min_len = float("inf")
        self.idx = float("inf")

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s, idx):
        node = self.root
        if len(s) < node.min_len:
            node.min_len = len(s)
            node.idx = idx
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

            if len(s)<node.min_len:
                node.min_len = len(s)
                node.idx = idx

    def query(self, s):
        node = self.root
        
        for c in s:
            if c not in node.children:
                break
            node = node.children[c]
        
        return node.idx

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()
        for i, word in enumerate(wordsContainer):
            trie.insert(word[::-1], i)
        
        ans = []
        for query in wordsQuery:
            ans.append(trie.query(query[::-1]))
        
        return ans

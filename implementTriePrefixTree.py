class TrieNode:
    def __init__(self):
        self.flag = 0
        self.childrens = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.childrens:
                curr.childrens[c] = TrieNode()
            curr = curr.childrens[c]
        curr.flag = 1

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.childrens:
                return False
            curr = curr.childrens[c]
        return curr.flag==1

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.childrens:
                return False
            curr = curr.childrens[c]
        return True



# Without Node using only hash
# class Trie:
#     def __init__(self):
#         self.root = {}
# 
#     def insert(self, word: str) -> None:
#         curr = self.root
#         for c in word:
#             if c not in curr:
#                 curr[c] = {}
#             curr = curr[c]
#         curr['#']=True

#     def search(self, word: str) -> bool:
#         curr = self.root
#         for c in word:
#             if c not in curr:
#                 return False
#             curr = curr[c]
#         return '#' in curr
# 
#     def startsWith(self, prefix: str) -> bool:
#         curr = self.root
#         for c in prefix:
#             if c not in curr:
#                 return False
#             curr = curr[c]
#         return True
        

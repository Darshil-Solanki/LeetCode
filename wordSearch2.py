
class TrieNode:
    def __init__(self):
        self.child = {}
        self.isWord = False
    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr=curr.child[c] 
        curr.isWord=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        m,n = len(board), len(board[0])
        for w in words:
            root.insert(w)
        res, hashMap = [], {}
        direction = [(0, 1),(0, -1), (1, 0), (-1, 0)]
        def dfs(currWord, node, i, j):
            if board[i][j] not in node.child:
                return
            node = node.child[board[i][j]]
            currWord += board[i][j]
            if node.isWord and currWord not in hashMap:
                res.append(currWord)
                hashMap[currWord]=True
            for dx, dy in direction:
                cx, cy = i+dx, j+dy
                if (-1<cx<m and -1<cy<n and 
                (cx, cy) not in seen):
                    seen.add((cx, cy))
                    dfs(currWord, node, cx, cy)
                    seen.remove((cx,cy))

            
        seen  = None
        for i in range(m):
            for j in range(n):
                seen = {(i,j)}
                dfs("", root, i, j)
        return res


# More Efficient on Runtime from submission
# class Trie:
#     def __init__(self):
#         self.dict = {}
    
#     def add(self,word):
#         cur = self.dict
#         for l in word:
#             if(l not in cur):
#                 cur[l] = {}
#             cur = cur[l]
#         cur['*'] = word
#         return

# class Solution:
#     # construct a dictionary for all words
#     # find all words from this matrix
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

#         def dfs(cur,a,b)-> None:
#             # nonlocal m
#             # nonlocal n
#             # nonlocal board
#             # nonlocal ret
#             val = board[a][b]
#             board[a][b] = '.'
#             if '*' in cur:
#                 ret.append(cur['*'])
#                 cur.pop('*', None)
#             if(a>0 and board[a-1][b] in cur):
#                 dfs(cur[board[a-1][b]],a-1,b)
#                 if(not cur[board[a-1][b]]):
#                     cur.pop(board[a-1][b],None)
#             if(a<m-1 and board[a+1][b] in cur):
#                 dfs(cur[board[a+1][b]],a+1,b)
#                 if(not cur[board[a+1][b]]):
#                     cur.pop(board[a+1][b],None)
#             if(b>0 and board[a][b-1] in cur):
#                 dfs(cur[board[a][b-1]],a,b-1)
#                 if(not cur[board[a][b-1]]):
#                     cur.pop(board[a][b-1],None)
#             if(b<n-1 and board[a][b+1] in cur):
#                 dfs(cur[board[a][b+1]],a,b+1)
#                 if(not cur[board[a][b+1]]):
#                     cur.pop(board[a][b+1],None)
#             board[a][b] = val

#             return None

#         m = len(board)
#         n = len(board[0])
#         ret = []
#         TrieDict = Trie()
#         for l in words:
#             TrieDict.add(l)
#         for i in range(m):
#             for j in range(n):
#                 val = board[i][j]
#                 if(val in TrieDict.dict):
#                     dfs(TrieDict.dict[val],i,j)

#         return list(ret)


# My initial Code
# class Trie:
#     def __init__(self):
#         self.root = {}
#     def insert(self, word):
#         curr = self.root
#         for c in word:
#             if c not in curr:
#                 curr[c] = {}
#             curr=curr[c] 
#         curr['#']=True
#     def search(self, word):
#         curr = self.root
#         for c in word:
#             if c not in curr:
#                 return (False, False)
#             curr=curr[c]
#         return (True, '#' in curr)

# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         trie = Trie()
#         m,n = len(board), len(board[0])
#         for w in words:
#             trie.insert(w)
#         res, hashMap = [], {}
#         direction = [(0, 1),(0, -1), (1, 0), (-1, 0)]
#         def dfs(curr, i, j):
#             curr += board[i][j]
#             prefix, wordMatch = trie.search(curr)
#             if wordMatch and curr not in hashMap:
#                 res.append(curr)
#                 hashMap[curr] = True

#             if prefix:
#                 for dx, dy in direction:
#                     cx, cy = i+dx, j+dy
#                     if -1<cx<m and -1<cy<n and (cx, cy) not in seen:
#                         seen.add((cx, cy))
#                         dfs(curr, cx, cy)
#                         seen.remove((cx,cy))

#         seen  = None
#         for i in range(m):
#             for j in range(n):
#                 seen = {(i,j)}
#                 dfs("", i,j)
#         return res

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        wordList, seen = set(wordList), set()
        if endWord not in wordList: return 0
        words = "abcdefghijklmnopqrstuvwxyz"
        queue = deque([beginWord])
        wordLength = len(beginWord)
        while queue:
            res+=1
            for i in range(len(queue)):
                node = queue.popleft()
                seen.add(node)
                for i in range(wordLength):
                    left, right = node[:i], node[i+1:]
                    for c in words:
                        curr = left+c+right
                        if curr==endWord:
                            return res+1
                        if curr in wordList and curr not in seen:
                            queue.append(curr)
        return 0

# Same idea but usage three set instead two which improve runtime
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         wordSet = set(wordList)
#         if endWord not in wordSet:
#             return 0
#         beginSet = {beginWord}
#         endSet = {endWord}
#         steps = 1
#         while beginSet and endSet:
#             wordSet -= beginSet
#             steps += 1
#             newSet = set()
#             for word in beginSet:
#                 for i in range(len(word)):
#                     left = word[:i]
#                     right = word[i+1:]
#                     for c in string.ascii_lowercase:
#                         newWord = left + c + right
#                         if newWord in wordSet:
#                             if newWord in endSet:
#                                 return steps
#                             newSet.add(newWord)
#             if len(beginSet) > len(endSet):
#                 beginSet = endSet
#                 endSet = newSet
#             else:
#                 beginSet = newSet
#         return 0

# neetcode solution usage adjacency list created with O(n*m) and overall tc 
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList: return 0 
#         nei = collections.defaultdict(list)
#         wordList.append(beginWord)
#         for word in wordList:
#             for j in range(len(word)):
#                 pattern = word[:j]+"*"+word[j+1:]
#                 nei[pattern].append(word)
#         seen = set(beginWord)
#         q = [beginWord]
#         res = 0
#         while q:
#             res+=1
#             for i in range(len(q)):
#                 word = q.pop(0)
#                 if word == endWord:
#                     return res
#                 for j in range(len(word)):
#                     pattern = word[:j]+"*"+word[j+1:]
#                     for neiWord in nei[pattern]:
#                         if neiWord not in seen:
#                             seen.add(neiWord)
#                             q.append(neiWord)
#         return 0

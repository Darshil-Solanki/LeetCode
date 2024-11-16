class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        wordList, seen = set(wordList), set()
        if endWord not in wordList: return 0
        words = "abcdefghijklmnopqrstuvwxyz"
        queue = [beginWord]
        wordLength = len(beginWord)
        while queue:
            curr_len = len(queue)
            res+=1
            for i in range(curr_len):
                node = queue.pop(0)
                seen.add(node)
                for i in range(wordLength):
                    left, right = node[:i], node[i+1:]
                    for c in words:
                        curr = left+c+right
                        if curr==endWord:
                            return res+1
                        if curr not in seen and curr in wordList:
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

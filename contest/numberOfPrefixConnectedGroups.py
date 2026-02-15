class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        group = defaultdict(int)
        for word in words:
            if len(word)<k:
                continue
            prefix = word[:k]
            group[prefix]+=1
        
        ans = 0
        for p, cnt in group.items():
            if cnt>1:
                ans += 1
        return ans

        # contest code
        # trie = defaultdict(dict)
        # root = trie
        # for word in words:
        #     curr = root   
        #     for c in word:
        #         if c not in curr:
        #             curr[c] = {}
        #         curr = curr[c]
        #     if "#" not in curr:
        #         curr["#"] = 0
        #     curr["#"] += 1

        # self.ans = 0
        # def dfs(tree, depth):
        #     if depth>=k:
        #         if len(tree)>1 or ("#" in tree and tree["#"]>1):
        #             self.ans += 1
        #             return
        #     for nei, subtree in tree.items():
        #         if nei=="#":
        #             continue
        #         dfs(subtree, depth+1)

        # dfs(root, 0)
        # return self.ans

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        ans = [0]*n
        temp_tree = defaultdict(list)
        tree = defaultdict(list)
        last = [-1] * 26

        for i in range(1, n):
            temp_tree[parent[i]].append(i)

        def dfs_create(node):
            c = ord(s[node]) - 97
            ancestor = last[c]

            if node and ancestor != -1:
                parent[node] = ancestor
            
            last[c] = node
            for nei in temp_tree[node]:
                dfs_create(nei)

            last[c] = ancestor
        
        def dfs_calc(node):
            ans[node] = 1

            for nei in tree[node]:
                ans[node] += dfs_calc(nei)
            
            return ans[node]

        dfs_create(0)

        for i in range(1, n):
            tree[parent[i]].append(i)
        
        dfs_calc(0)
        
        return ans

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        self.ans = float("-inf")
        # creating tree
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        distance_from_bob = [0]*n
        def dfs(node, parent, time):
            ans = 0
            mx_child = float("-inf")

            # find the node distances from bob
            distance_from_bob[node] = 0 if node == bob else n

            for ch in tree[node]:
                if ch != parent:
                    mx_child = max(mx_child, dfs(ch, node, time+1))
                    distance_from_bob[node] = min(
                        distance_from_bob[node], distance_from_bob[ch]+1
                    )


             # Alice reaches the node first
            if distance_from_bob[node] > time:
                ans += amount[node]
            # Alice and Bob reach the node at the same time
            elif distance_from_bob[node] == time:
                ans += amount[node] // 2

            # Return max income of leaf node
            return (
                ans if mx_child == float("-inf") else ans + mx_child
            )
            
        
        return dfs(0, 0, 0)

        # # finding bob path
        # def find_bob_path(node, time):
        #     self.bob_path[node] = time
        #     seen[node] = True

        #     if node==0:
        #         return True
        #     for ch in tree[node]:
        #         if not seen[ch]:
        #             if find_bob_path(ch, time+1):
        #                 return True
        #     self.bob_path.pop(node, None)
        #     return False
        
        # self.bob_path = {}
        # seen = [False]*n
        # find_bob_path(bob, 0)
        
        # seen = [False]*n

        # # traversing alice using dfs
        # def dfs(node, time, income):
        #     seen[node] = True

        #     # Alice reach the node first
        #     if (node not in self.bob_path or time<self.bob_path[node]):
        #         income += amount[node]
        #     # Alice and Bob reach the node at same time
        #     elif (self.bob_path[node] == time):
        #         income += amount[node]//2
            
        #     if len(tree[node])==1 and node!=0:
        #         self.ans = max(self.ans, income)
            
        #     for ch in tree[node]:
        #         if not seen[ch]:
        #             dfs(ch, time+1, income)

        
        # dfs(0, 0, 0)
        # return self.ans

        # traversing alice using bfs

        # queue = deque([(0, 0, 0)])
        # while queue:
        #     node, time, income = queue.popleft()
            
        #     # Alice reach the node first
        #     if (node not in self.bob_path or time<self.bob_path[node]):
        #         income += amount[node]
        #     # Alice and Bob reach the node at same time
        #     elif (self.bob_path[node] == time):
        #         income += amount[node]//2

        #     if len(tree[node])==1 and node!=0:
        #         self.ans = max(self.ans, income)
            
        #     for ch in tree[node]:
        #         if not seen[ch]:
        #             queue.append((ch, time+1, income))

        #     seen[node] = True

        # return self.ans        

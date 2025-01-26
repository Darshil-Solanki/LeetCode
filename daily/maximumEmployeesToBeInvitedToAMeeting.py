class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:

        # take help from hint and solutions
        n = len(favorite)
        indeg, chain_len, seen = [0]*n, [0]*n, [False]*n
        queue = deque()

        # counting favorite person node indegree
        for f in favorite:
            indeg[f]+=1
        
        # using topologic sorting for finding len of all acyclic edges
        for i, deg in enumerate(indeg):
            if not deg:
                queue.append(i)
        
        while queue:
            u = queue.popleft()
            seen[u]=True
            v = favorite[u]
            chain_len[v] = max(chain_len[v], chain_len[u]+1)
            indeg[v]-=1
            if not indeg[v]:
                queue.append(v)
        
        # detect cycle and calculate results
        max_cycle, pair_chains = 0, 0
        for i in range(n):
            if seen[i]:
                continue
            cycle_len = 0
            curr = i
            while not seen[curr]:
                seen[curr]=True
                curr = favorite[curr]
                cycle_len+=1
            if cycle_len==2:
                pair_chains+= 2+chain_len[i]+chain_len[favorite[i]]
            else:
                if cycle_len>max_cycle: max_cycle = cycle_len
        return max(max_cycle, pair_chains)

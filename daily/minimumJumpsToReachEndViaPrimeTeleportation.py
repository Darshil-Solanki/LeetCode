MX = 1_000_001
factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not factors[i]:
        for j in range(i, MX, i):
            factors[j].append(i)


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        edges = defaultdict(list)
        for i, num in enumerate(nums):
            if len(factors[num]) == 1:
                edges[num].append(i)
        res = 0
        seen = [False] * n
        seen[-1] = True
        queue = deque([n - 1])
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                if i == 0:
                    return res
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    queue.append(i - 1)
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    queue.append(i + 1)
                for p in factors[nums[i]]:
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            queue.append(j)
                    edges[p].clear()
            res += 1

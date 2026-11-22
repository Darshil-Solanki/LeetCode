class Solution:
    def earliestActivationTimes(self, n: int, edges: list[list[int]], requiredSignals: list[int]) -> list[int]:
        graph = defaultdict(list)
        active = [-1]*n
        active[0] = 0

        for u, v, d in edges:
            graph[u].append((v, d))

        queue = [(0, 0)]
        waiting_signal = [SortedList() for _ in range(n)]
        curr_signals = [set() for _ in range(n)]
        while queue:
            time, node = heappop(queue)
            while waiting_signal[node] and waiting_signal[node][0][0]<=time:
                _, sender = waiting_signal[node].pop(0)
                curr_signals[node].add(sender)
            if len(curr_signals[node])>=requiredSignals[node]:
                active[node] = min(time, (active[node] if active[node] != -1 else float("inf")))
            if active[node] != -1:
                for nei, delay in graph[node]:
                    if active[nei]==-1:
                        heappush(queue, (time+delay, nei))
                        waiting_signal[nei].add((time+delay, node))

        return active
                

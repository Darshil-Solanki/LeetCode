class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # copied from solutions
        r_queue = deque([])
        d_queue = deque([])
        n=len(senate)
        for i, vote in enumerate(senate):
            if vote=="R":
                r_queue.append(i)
            else:
                d_queue.append(i)
        while r_queue and d_queue:
            r = r_queue.popleft()
            d = d_queue.popleft()
            if r<d:
                r_queue.append(n+r)
            else:
                d_queue.append(n+d)
        return "Radiant" if r_queue else "Dire"

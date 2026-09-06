class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        queue = deque(list(s))

        for _ in range(n):
            score = 0 
            for i in range(n-1):
                if queue[i]==queue[i+1]:
                    score += 1
            if score==k:
                ans += 1
            queue.append(queue.popleft())

        return ans

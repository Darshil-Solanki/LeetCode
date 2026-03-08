class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        ans = len(capacity)
        min_cap = float("inf")
        for i, c in enumerate(capacity):
            if itemSize<=c<min_cap:
                ans = i
                min_cap = c

        return -1 if ans==len(capacity) else ans
        

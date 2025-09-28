class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)
        if k == n: return 1
        u_final_pos = {}
        left_prefix, right_prefix = [(0, 0)], [(0,0)]
        last = (0, 0)
        for c in s:
            match c:
                case "U":
                    last = (last[0], last[1]+1)
                    left_prefix.append(last)
                case "D":
                    last = (last[0], last[1]-1)
                    left_prefix.append(last)
                case "L":
                    last = (last[0]-1, last[1])
                    left_prefix.append(last)
                case "R":
                    last = (last[0]+1, last[1])
                    left_prefix.append(last)
        
        last = (0, 0)
        for c in s[::-1]:
            match c:
                case "U":
                    last = (last[0], last[1]+1)
                    right_prefix.append(last)
                case "D":
                    last = (last[0], last[1]-1)
                    right_prefix.append(last)
                case "L":
                    last = (last[0]-1, last[1])
                    right_prefix.append(last)
                case "R":
                    last = (last[0]+1, last[1])
                    right_prefix.append(last)
        
        for i in range(n-k+1):
            lx, ly = left_prefix[i]
            rx, ry = right_prefix[n-i-k]
            u_final_pos[(lx+rx, ly+ry)] = True
        
        return len(u_final_pos)
    

# from submission: sliding window type(finding diff. window points instead of final point) 
# from typing import Set, Tuple

# def _step(c: str) -> Tuple[int, int]:
#     if c == 'U': return (0, 1)
#     if c == 'D': return (0, -1)
#     if c == 'L': return (-1, 0)
#     return (1, 0)  # 'R'

# class Solution:
#     def distinctPoints(self, s: str, k: int) -> int:
#         n = len(s)
#         dx = dy = 0
#         for i in range(k):
#             x, y = _step(s[i])
#             dx += x; dy += y
#         seen: Set[Tuple[int,int]] = {(dx, dy)}
#         for i in range(1, n - k + 1):
#             rx, ry = _step(s[i-1])
#             ax, ay = _step(s[i+k-1])
#             dx -= rx; dy -= ry
#             dx += ax; dy += ay
#             seen.add((dx, dy))
#         return len(seen)

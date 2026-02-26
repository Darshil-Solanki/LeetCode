class Solution:
    def numSteps(self, s: str) -> int:
        curr = deque(map(int, s))
        ans = 0
        while len(curr)>1:
            if curr[-1]:
                n = len(curr)
                curr[-1] = 0
                for i in range(-2, -n-1, -1):
                    if curr[i]:
                        curr[i]=0
                        continue
                    curr[i]=1
                    break
                else:
                    curr.appendleft(1)
            else:
                curr.pop()
            ans += 1
        
        return ans

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1]=="1":
            return False
        
        n = len(s)
        queue = deque([0])
        prev_right = 0

        while queue:
            i = queue.popleft()
            if i == n-1:
                return True
            left = i + minJump
            right = i + maxJump
            for j in range(max(prev_right+1, left), min(right+1, n)):
                if s[j]=="0":
                    queue.append(j)
            prev_right  = right

        return False
    
        # TLE
        # if s[-1]=="1":
        #     return False

        # @cache
        # def dp(i):
        #     if i == n-1:
        #         return True

        #     for j in range(min(i+maxJump, n-1), i+minJump-1, -1):
        #         if s[j]=="0" and dp(j):
        #             return True
        #     return False

        # return dp(0)

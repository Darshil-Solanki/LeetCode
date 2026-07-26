class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if 9*n<s:
            return -1

        def backtrack(i, num, tot):
            if i == n:
                if tot == s:
                    return num
                return -1
                
            ans = -1
            for j in range(10):
                ans = max(ans, backtrack(i+1, num*10+j, tot+j))

            return ans

        return backtrack(0, 0, 0)
            

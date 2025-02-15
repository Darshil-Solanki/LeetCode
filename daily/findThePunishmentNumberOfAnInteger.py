map = {}
class Solution:
    def backtrack(self, x, target):
        # from one of the solution
        if x==target: return True
        if x==0: return target==0
        for j in (10, 100, 1000):
            if self.backtrack(x//j, target-x%j): return True
        return False

    def validNum(self, n):
        if n in map: return map[n]
        result=False
        square = n*n
        result = self.backtrack(square, n)
        map[n]=result
        return result

    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            if i in map:
                if map[i]:
                    ans+=i*i
                continue
            if i%9==0 or i%9==1:        # Optimization trick from discussion
                if self.validNum(i):
                    ans+=i*i
            else:
                map[i]=False
        return ans

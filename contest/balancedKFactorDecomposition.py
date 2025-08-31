class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        self.factor = []
        self.diff = float("inf")
        
        def check(curr_f):
            mn, mx = min(curr_f), max(curr_f)
            if mx-mn<self.diff:
                self.factor = curr_f[:]
        
        def backtrack(n, k, start, curr_factor):
            if k==1:
                if n>=start:
                    curr_factor.append(n)
                    check(curr_factor)
                    curr_factor.pop()
                return
            for i in range(start, int(sqrt(n))+1):
                if n%i==0:
                    curr_factor.append(i)
                    backtrack(n//i, k-1, i, curr_factor)
                    curr_factor.pop()
        
        backtrack(n, k, 1, [])
        return self.factor

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def solve(num):
            base = i = 1
            cnt = 0
            while base<=num:
                cnt += ((i+1)//2)*(min(base*2-1, num)-base+1)
                i += 1
                base *= 2
            return cnt

        ans = 0
        for l, r in queries:
            ans += (solve(r)-solve(l-1)+1)//2
        
        return ans

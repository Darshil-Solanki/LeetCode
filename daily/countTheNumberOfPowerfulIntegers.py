class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if finish<int(s): return 0
        low, high = str(start), str(finish)
        n = len(high)
        pre_len = n-len(s)
        low = low.zfill(n)

        @cache
        def dfs(i, limit_low, limit_high):
            if i==n:
                return 1
            
            l = int(low[i]) if limit_low else 0
            h = int(high[i]) if limit_high else 9
            res = 0
            if i<pre_len:
                for digit in range(l, min(h, limit)+1):
                    res += dfs(i+1, limit_low and digit==l, limit_high and digit==h)
            else:
                x = int(s[i-pre_len])
                if l<= x <= min(h, limit):
                    res = dfs(i+1, limit_low and x==l, limit_high and x==h)
                    
            return res

        return dfs(0, True, True)
        # copied from editorial we are counting prefix that can be formed in limit

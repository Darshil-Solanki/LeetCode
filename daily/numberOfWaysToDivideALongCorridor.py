class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007
        
        cache = [[-1]*3 for _ in range(len(corridor))]

        def count(i, seats):
            if i == len(corridor):
                return 1 if seats==2 else 0
            
            if cache[i][seats] != -1:
                return cache[i][seats]
            
            if seats == 2:
                if corridor[i] == "S":
                    ans = count(i+1, 1)
                else:
                    ans = (count(i+1, 0) + count(i+1, 2))%MOD
            else:
                if corridor[i] == "S":
                    ans = count(i+1, seats+1)
                else:
                    ans = count(i+1, seats)
            
            cache[i][seats] = ans
            return ans
        
        return count(0, 0)

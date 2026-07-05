class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        n = len(s1)
        if n==1:
            if s1==s2:
                return 0
            if s1=="0" and s2=="1":
                return 1
            return -1
        ans = 0
        pair_01 = 0
        pair_10 = 0
        for s, t in zip(s1, s2):
            if s=="1" and t=="0":
                pair_10 += 1
            else:
                if pair_10:
                    ans += pair_10//2 + (pair_10%2)*2
                    pair_10 = 0
                if s=="0" and t=="1":
                    pair_01 += 1
        
        if pair_10:
            ans += pair_10//2 + (pair_10%2)*2
        ans += pair_01
        return ans

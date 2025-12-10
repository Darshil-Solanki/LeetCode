class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
        
        ans, MOD = 1, 1_000_000_007
        for i in range(2, len(complexity)):
            ans = ans*i % MOD
        
        return ans

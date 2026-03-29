class Solution:
    def countVisiblePeople(self, n, pos, k):
        MOD = 1_000_000_007
        if not k:
            return 2
        return 2 * comb(n - 1, k) % MOD

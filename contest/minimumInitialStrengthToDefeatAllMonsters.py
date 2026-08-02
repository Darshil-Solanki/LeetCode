class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n = len(monsters)
        bonus = [0]*n
        ans = sum(monsters)
        
        for l, r, v in boosts:
            bonus[l] += v
            if r+1<n:
                bonus[r+1] -= v

        temp = 0
        for i in range(n):
            temp += bonus[i]
            bonus[i] = temp

        for i in range(n-1, -1, -1):
            if bonus[i]>=monsters[i]:
                ans -= monsters[i]
                continue
            ans -= bonus[i]
            break

        return ans

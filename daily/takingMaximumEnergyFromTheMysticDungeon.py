class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = float("-inf")

        for i in range(n-k, n):
            tot, j = 0, i
            while j>-1:
                tot+=energy[j]
                if tot>ans:
                    ans = tot
                j -= k

        return ans

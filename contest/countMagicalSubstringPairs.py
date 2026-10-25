class Solution:
    def countMagicalPairs(self, s: str) -> int:
        n = len(s)
        ans = 0

        for j in range(n-1):
            left_counts = [0]*27
            right_counts = [0]*27

            seen = set()
            for i in range(j, -1, -1):
                seen.add(s[i])
                left_counts[len(seen)] += 1

            seen.clear()
            for k in range(j+1, n):
                seen.add(s[k])
                right_counts[len(seen)] += 1

            ans += sum(left_counts[dc] * right_counts[dc] for dc in range(1, 27))

        return ans

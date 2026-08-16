class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n, m = len(skill), len(station)
        if n == 1:
            return 0
        
        left = [0] * n
        pos = 0
        for i in range(n):
            while station[pos] != skill[i]:
                pos += 1
            left[i] = pos
            pos += 1
        
        right = [0]*n
        pos = m - 1
        for i in range(n-1 , -1, -1):
            while station[pos] != skill[i]:
                pos -= 1
            right[i] = pos
            pos -= 1
        
        return max(right[i+1] - left[i] for i in range(n-1))

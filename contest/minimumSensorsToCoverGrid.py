class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        return ceil(n/(2*k+1)) * ceil(m/(2*k+1))

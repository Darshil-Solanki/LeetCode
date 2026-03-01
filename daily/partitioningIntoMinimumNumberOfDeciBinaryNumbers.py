class Solution:
    def minPartitions(self, n: str) -> int:
        # return max(map(int, n))
        for d in "987654321":
            if d in n:
                return int(d)

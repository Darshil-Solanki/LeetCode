class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, (n//2)+1):
            if not str(i).count("0")+str(n-i).count("0"):
                return [i, n-i]

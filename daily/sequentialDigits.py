class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        low_length, high_length = len(str(low)), len(str(high))
        for l in range(low_length, high_length+1):
            for i in range(1, 10-l+1):
                num = int("".join(str(j) for j in range(i, i+l)))
                if low <= num <= high:
                    ans.append(num)
                    continue

        ans.sort()
        return ans

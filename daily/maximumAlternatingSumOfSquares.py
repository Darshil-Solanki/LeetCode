class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        square_values = [num*num for num in nums]
        square_values.sort()
        n = len(square_values)
        return sum(square_values[n//2 : ]) - sum(square_values[:n//2])

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        ans = 0
        low, high, curr = 0, 0, 0

        for diff in differences:
            curr += diff
            low, high = min(low, curr), max(high, curr)
            if high-low > upper-lower:
                return 0
            
        return (upper-lower) - (high-low)+1

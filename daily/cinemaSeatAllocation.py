class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        left, middle, right = 0b11110000, 0b11000011, 0b00001111
        used_row = defaultdict(int)
        for r, c in reservedSeats:
            if 1 < c < 10:
                used_row[r] |= 1<<(c - 2)

        ans = (n - len(used_row)) * 2
        for row, bitmask in used_row.items():
            if (
                (bitmask | left) == left or (bitmask | middle) == middle or 
                (bitmask | right) == right
            ):
                ans += 1
        
        return ans

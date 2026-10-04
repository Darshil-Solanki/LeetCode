class Solution:
    def minRotations(self, s: str) -> int:
        pointer = 0
        ans = 0
        
        for c in s:
            digit = int(c)
            if pointer == digit:
                continue
            if pointer < digit:
                ans += min(digit-pointer, pointer+10-digit)
            else:
                ans += min(pointer-digit, 10-pointer+digit)
            pointer = digit

        return ans

class Solution:
    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
        if value == 1:
            return 1 if n == 1 else -1
        
        def min_prime_factor(value):
            i = 3

            while i<=isqrt(value):
                if value % i == 0:
                    return i
                i += 2
            
            return value
        
        min_factor = min_prime_factor(value)
        
        max_left = (value - 2) // 2 if value % 2 == 0 else (value - min_factor) // 2

        if index > max_left:
            return -1
        
        steps = n - index - 1
        if steps == 0:
            return value
        
        if value % 2 == 0:
            return value + steps * 2
        
        return value + min_factor + (steps - 1) * 2

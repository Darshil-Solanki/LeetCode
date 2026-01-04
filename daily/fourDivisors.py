class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        def sum_one(n):
            p = round(n ** (1/3))
            if p ** 3 == n and is_prime(p):
                return 1 + p + p*p + p*p*p

            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    a, b = i, n // i
                    if a != b and is_prime(a) and is_prime(b):
                        return 1 + a + b + n
                    return -1
            return -1

        for num in nums:
            sum_1 = sum_one(num)
            if sum_1!=-1:
                ans += sum_1

        return ans

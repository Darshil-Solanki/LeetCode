class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        k_palindrome_set = set()
        base = 10 ** ((n-1)//2)
        skip = n & 1

        # generating all palindrome of length n that are divisible by k
        for i in range(base, base*10):
            s = str(i)
            s += s[::-1][skip:]
            palindrome_int = int(s)
            if palindrome_int % k == 0:
                sorted_s = "".join(sorted(s))
                k_palindrome_set.add(sorted_s)
        
        # calculating combinations of good integers using PnC
        fac = [factorial(i) for i in range(n+1)]
        ans = 0
        for s in k_palindrome_set:
            count = [0]*10
            for c in s:
                count[int(c)]+=1
            
            tot = (n-count[0]) * fac[n-1]
            for x in count:
                tot//=fac[x]
            ans += tot
        
        return ans

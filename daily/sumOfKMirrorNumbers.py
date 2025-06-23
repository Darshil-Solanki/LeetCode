class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def is_palindrome(num):
            digit = [] # will have num in reverse order in base k
            while num:
                digit.append(num % k)
                num //= k
            return digit == digit[::-1]
        
        left, cnt, ans = 1, 0, 0
        while cnt<n:
            right = left * 10

            for flag in [0, 1]: # 0 for odd, 1 for even
                for num in range(left, right):
                    if cnt == n: break
                    
                    combined = num
                    x = num if flag else num // 10
                    while x:
                        combined = combined*10 + x%10
                        x //= 10
                    if is_palindrome(combined):
                        cnt += 1
                        ans += combined
            left = right
        
        return ans

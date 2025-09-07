import array
prefix_palindrome = array.array('I', [0, 2, 3])
temp = 3
for b_length in range(3, 51):
    inside = b_length-2
    temp += 1<<((inside+1)//2)
    prefix_palindrome.append(temp)

class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if not n: return 1
        if n==1: return 2
        ans = 0
        
        length = n.bit_length()
        ans += prefix_palindrome[length-1]
        bit_arr = [int(i) for i in bin(n)[2:]]
        half = (length+1)//2
        for i in range(1, half):
            if bit_arr[i]:
                ans += 1<<(half-i-1)
        ans += bit_arr[:half][::-1]  <= bit_arr[-half:]
        return ans

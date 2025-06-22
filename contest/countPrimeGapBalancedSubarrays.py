MAX = 50_001
seive = [True] * MAX
seive[0] = seive[1] = False

for num in range(2, int(MAX**0.5)+1):
    if seive[num]:
        for comp in range(num*num, MAX, num):
            seive[comp] = False

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        left = ans = 0
        prev = curr = -1
        prime_window = Counter()

        for right, num in enumerate(nums):
            if seive[num]:
                prev = curr
                curr = right
                prime_window[num] += 1

            while prime_window and max(prime_window) - min(prime_window)>k:
                if seive[nums[left]]:
                    prime_window[nums[left]] -= 1
                    if prime_window[nums[left]] == 0:
                        del prime_window[nums[left]]
                left += 1
            
            if prime_window.total()>=2:
                ans += (prev-left+1)
        
        return ans

is_prime = [True]*1_00_001
is_prime[0] = is_prime[1] = False

for num in range(2, int(sqrt(1_00_001))+1):
    if is_prime[num]:
        for comp in range(num*num, 1_00_001, num):
            is_prime[comp] = False

class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        ans = 0
        left = 0
        prime_fact_cnt = defaultdict(int)

        @lru_cache
        def get_prime_fact(num):
            ans = []
            for i in range(2, int(sqrt(num))+1):
                if not num:
                    break
                if num%i==0:
                    ans.append(i)
                    while num%i==0:
                        num //= i
            if num and is_prime[num]:
                if not ans or ans[-1]!=num:
                    ans.append(num)
            return ans if ans else [num]
        
        for right, num in enumerate(nums):
            for f in get_prime_fact(num):
                prime_fact_cnt[f] += 1

            while len(prime_fact_cnt)>k:
                for f in get_prime_fact(nums[left]):
                    prime_fact_cnt[f] -= 1
                    if not prime_fact_cnt[f]:
                        del prime_fact_cnt[f]
                left += 1
                if len(prime_fact_cnt)<=k:
                    ans = max(ans, right-left+1)

            if len(prime_fact_cnt)<=k:
                ans = max(ans, right-left+1)

        return ans

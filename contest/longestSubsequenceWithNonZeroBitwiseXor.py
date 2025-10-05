class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        all_zero = True
        for x in nums:
            xor ^= x
            if x!=0:
                all_zero = False

        if xor!=0:
            return len(nums)
        return (len(nums)-1) if not all_zero else 0 

        # bit = [0]*32
        # all_zero = True
        # for n in nums:
        #     if n:
        #         all_zero = False
        #     i = 0
        #     while n>0:
        #         if n & 1:
        #             bit[i] += 1
        #         i += 1
        #         n >>= 1

        # for b in bit:
        #     if b%2:
        #         return len(nums)
        # return 0  if all_zero else len(nums)-1 

        # nums.sort()
        # one_less = (1<<(nums[-1].bit_length()-1))-1
        # i = bisect_right(nums, one_less)
        # ans = i
        # last_bit = n - i
        # if last_bit%2 != 0:
        #     return n
        # remaining = 0
        # for j in range(i, n):
        #     remaining ^= nums[j]
        # if remaining:
        #     return n
        # ans += last_bit-1
        # return ans
        

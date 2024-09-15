class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = []
        for i, val in counter.items():
            if val>1:
                res.append(i)
        return res
        #Better Solution without extra space with bitmasking
        # n = len(nums) - 2  # Because there are two extra numbers
    
        # # Step 1: XOR all elements in nums and numbers from 0 to n-1
        # xor_all = 0
        # for num in nums:
        #     xor_all ^= num
        # for i in range(n):
        #     xor_all ^= i
        
        # # Step 2: Find the rightmost set bit in xor_all
        # rightmost_set_bit = xor_all & -xor_all
        
        # # Step 3: Partition the numbers into two groups based on the rightmost set bit
        # xor1, xor2 = 0, 0
        # for num in nums:
        #     if num & rightmost_set_bit:
        #         xor1 ^= num
        #     else:
        #         xor2 ^= num
        
        # for i in range(n):
        #     if i & rightmost_set_bit:
        #         xor1 ^= i
        #     else:
        #         xor2 ^= i
        
        # # The two numbers found are the duplicates
        # return [xor1, xor2]

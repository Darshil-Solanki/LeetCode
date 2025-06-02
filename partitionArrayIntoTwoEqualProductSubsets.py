class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        nums.sort()
        n = len(nums)

        def backtrack(i, product, used):
            if i == n:
                if product==target:
                    remaining_product = 1
                    for i, num in enumerate(nums):
                        if not used[i]:
                            remaining_product *= num
                    if remaining_product == target:
                        return True
                return False
            if product>target:
                return False

            used[i] = 1
            if backtrack(i+1, product*nums[i], used):
                used[i] = 0
                return True
            used[i] = 0
            if backtrack(i+1, product, used):
                return True
            return False
        
        return backtrack(0, 1, [0]*n)

        # checking from entire multiplication and all element are divisor of target
        # return prod(nums) == target ** 2 and not [i for i in nums if target % i != 0]
        

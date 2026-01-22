class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        
        while len(nums)>1:
            non_increasing = False
            min_sum = float("inf")
            target_idx = -1

            for i in range(len(nums)-1):
                pair_sum = nums[i] + nums[i+1]

                if nums[i]>nums[i+1]:
                    non_increasing = True
                if pair_sum<min_sum:
                    min_sum = pair_sum
                    target_idx = i

            if not non_increasing:
                break
            ans += 1
            nums[target_idx] = min_sum
            nums.pop(target_idx+1)

        return ans

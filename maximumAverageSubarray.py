class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tot = 0
        l=0
        avg = float('-inf')
        for r in range(len(nums)):
            tot+=nums[r]
            if r+1-l>=k:
                avg = tot/k if tot/k>avg else avg
                tot-=nums[l]
                l+=1
        return avg

        # Better way doing same thing 
        def findMaxAverage(self, nums, k):
            max_val = sum(nums[0:k])
            current_sum = max_val

            for i in range(1,(len(nums) - k)+1):
                current_sum = current_sum - nums[i-1] + nums[i+k-1]
                max_val = max(max_val,current_sum)

            return max_val/k

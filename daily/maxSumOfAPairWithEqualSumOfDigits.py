class Solution:
    def get_digit_sum(self, n):
        tot=0
        while n>0:
            tot += (n%10)
            n//=10
        return tot

    def maximumSum(self, nums: List[int]) -> int:
        digitSum = defaultdict(int)
        maxSum = -1
        nums.sort()

        for i, n in enumerate(nums):
            curr_sum = self.get_digit_sum(n)
            if curr_sum in digitSum:
                prev_num=nums[digitSum[curr_sum]]
                if prev_num+n>maxSum: maxSum = prev_num+n
            digitSum[curr_sum]=i
                
        return maxSum
    
    # Faster approach
    # By storing both number as pair no need to sort 
    # def maximumSum(self, nums: List[int]) -> int:
    #     d, mx = dict(), -1

    #     for num in nums:
    #         sm, n = 0, num
    #         while n:
    #             sm += n % 10
    #             n //= 10
    #         if sm in d:
    #             if d[sm][0] <= num:
    #                 d[sm][1] = d[sm][0]
    #                 d[sm][0] = num
    #             elif d[sm][1] < num:
    #                 d[sm][1] = num
    #         else:
    #             d[sm] = [num, -1]
        
    #     for k in d:
    #         if d[k][1] != -1: 
    #             sm = d[k][0] + d[k][1]
    #             if sm > mx:
    #                 mx = sm
        
    #     return mx

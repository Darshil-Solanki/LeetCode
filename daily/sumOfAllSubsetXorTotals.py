class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        self.ans = 0
        
        def backtrack(i, tot):
            if i==n:
                self.ans+=tot
                return
            
            ans = 0
            backtrack(i+1, tot^nums[i]) #include
            backtrack(i+1, tot) #not include

            return ans
        
        backtrack(0, 0)

        return self.ans

        # faster approach to calculate accumulated xor using or and all combination
        # ans = 0
        # for i in nums:
        #     ans |= i
        # return ans << (len(nums)-1)
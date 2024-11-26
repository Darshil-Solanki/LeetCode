class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        minJump = [float('inf')]*n
        minJump[n-1] =  0
        for i in range(n-2, -1, -1):
            if nums[i]:
                minJump[i] = 1+min(minJump[i+1:i+nums[i]+1])
        print(minJump)
        return minJump[0]
    
    # Better Way 
    # def jump(self, nums: List[int]) -> int:
    #     jump = 0
    #     cur_jump = 0
    #     max_jump = 0
    #     for i in range(len(nums)):
    #         if cur_jump < i:
    #             jump += 1
    #             cur_jump = max_jump
    #         max_jump = max(max_jump, i+nums[i])
    #     return jump

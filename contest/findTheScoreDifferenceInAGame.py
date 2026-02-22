class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        flag = True
        one, two = 0, 0

        for i, num in enumerate(nums):
            if num%2:
                flag = not flag
            if (i+1)%6==0:
                flag = not flag
            if flag:
                one += num
            else:
                two += num

        return one-two

class Solution:
    def minElement(self, nums: List[int]) -> int:
        minVal = float('inf')
        for i in nums:
            curr = self.getSum(i)
            minVal = min(minVal,curr)
        return minVal

    def getSum(self, num):
        tot = 0
        while num>0:
            tot += num%10
            num=int(num//10)
        return tot

        

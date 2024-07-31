class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        total = sum(nums)
        sSum , dSum = 0, 0
        bobSum = 0
        for i in nums:
            if i<10:
                sSum+=i
            else:
                dSum+=i
        return dSum>total-dSum or sSum>total-sSu

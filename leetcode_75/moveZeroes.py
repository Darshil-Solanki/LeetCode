class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIndex = -1
        numIndex, n = 0, len(nums)
        while numIndex<n:
            curr = nums[numIndex]
            if not curr: 
                if zeroIndex == -1:
                    zeroIndex = numIndex
                numIndex+=1
            if curr:
                if zeroIndex > -1:
                    nums[zeroIndex], nums[numIndex] = curr, 0
                    numIndex = zeroIndex+1
                    zeroIndex = -1
                else:
                    numIndex+=1
        
        # fastest method just overwrite all 0 element end put all zeroes at end
        # lastNonZeroIndex = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[lastNonZeroIndex] = nums[i]
        #         lastNonZeroIndex += 1
        # for i in range(lastNonZeroIndex, len(nums)):
        #     nums[i] = 0

        # Two pointer method
        # i = 0
        # n = len(nums)
        # while i < n:
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        #         n -= 1
        #     else:
        #         i+=1

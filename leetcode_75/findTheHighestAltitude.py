class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = 0
        maxRes = 0
        for i, g in enumerate(gain):
            prefixSum = prefixSum+g
            if prefixSum>maxRes: maxRes = prefixSum
        return maxRes

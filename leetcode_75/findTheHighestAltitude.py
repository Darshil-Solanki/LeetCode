class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = [0]
        maxRes = 0
        for i, g in enumerate(gain):
            prefixSum.append(prefixSum[i]+g)
            if prefixSum[i+1]>maxRes: maxRes = prefixSum[i+1]
        return maxRes

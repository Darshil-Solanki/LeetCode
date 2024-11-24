class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        nextPrefixSum, previousPrefixSum = [nextCost[0]], [previousCost[0]]
        for i in range(1, 26):
            nextPrefixSum.append(nextPrefixSum[i-1]+nextCost[i])
        for i in range(1, 26):
            previousPrefixSum.append(previousPrefixSum[i-1]+previousCost[i])
        cost = 0
        for sc, st in zip(s, t):
            if sc==st:
                continue
            scI, stI = ord(sc)-97, ord(st)-97
            leftCost, rightCost = 0, 0
            if scI<stI:
                leftCost = previousPrefixSum[scI]+previousPrefixSum[25]-previousPrefixSum[stI] 
                rightCost = nextPrefixSum[stI-1]-(nextPrefixSum[scI-1] if scI>0 else 0)
            else:
                leftCost = previousPrefixSum[scI] - previousPrefixSum[stI] 
                rightCost = nextPrefixSum[25]-nextPrefixSum[scI-1] + (nextPrefixSum[stI-1] if stI>0 else 0)
            cost += min(leftCost, rightCost)
        return cost

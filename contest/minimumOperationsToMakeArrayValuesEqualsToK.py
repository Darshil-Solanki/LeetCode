class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        newNums = list(sorted(set(nums)))
        if newNums[0]<k: return -1
        return len(newNums)-1 if newNums[0]==k else len(newNums)

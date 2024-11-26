class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def xSum(arr):
            freq = Counter(arr)
            most_common = heapq.nlargest(x, freq.items(), key=lambda item: (item[1], item[0]))
            return sum(value*count for value, count in most_common)

        res = []  
        for i in range(len(nums)-k+1):
            res.append(xSum(nums[i:i+k]))
        return res

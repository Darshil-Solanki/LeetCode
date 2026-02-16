class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        prefix_sum = []
        temp = 0
        for n in nums:
            temp += n
            prefix_sum.append(temp)

        suffix_min = deque([])
        minimum = float("inf")
        for n in nums[::-1]:
            if n<minimum:
                minimum = n
            suffix_min.insert(0, minimum)

        score = float("-inf")
        for i in range(len(nums)-1):
            score = max(score, prefix_sum[i]-suffix_min[i+1])
            
        return score

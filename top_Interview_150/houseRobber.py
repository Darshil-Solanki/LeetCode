class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            max_rob = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = max_rob
        return rob2

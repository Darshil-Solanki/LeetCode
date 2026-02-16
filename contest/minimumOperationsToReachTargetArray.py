class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        new_list = set()
        
        for n, t in zip(nums, target):
            if n!=t:
                new_list.add(n)

        return len(new_list)

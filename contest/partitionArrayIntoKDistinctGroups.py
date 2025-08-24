class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n%k:
            return False
        g = len(nums)//k
        cnt = Counter(nums)
        for val in cnt.values():
            if val>g:
                return False
        return True

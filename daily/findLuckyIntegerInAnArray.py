class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        
        cnt = Counter(arr)
        for val, count in cnt.items():
            if val == count:
                ans = max(ans, val)
        
        return ans

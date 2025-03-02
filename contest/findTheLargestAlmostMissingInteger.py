class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        ans = -1
        map = defaultdict(int)
        for i in range(len(nums)-k+1):
            for n in set(nums[i:i+k]):
                map[n]+=1
        for k, v in map.items():
            if v==1 and k>ans:
                ans = k
        return ans

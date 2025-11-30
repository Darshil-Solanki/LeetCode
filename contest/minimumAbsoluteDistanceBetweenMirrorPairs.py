class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ans = float("inf")
        idx = Counter()

        def reverse(num):
            rev = 0
            while num>0:
                rev *= 10 
                rev += num%10
                num //= 10

            return rev
        
        for j, num in enumerate(nums[::-1]):
            reverse_num = reverse(num)
            if reverse_num in idx:
                ans = min(ans, j-idx[reverse_num])
            
            idx[num] = j
        
        return -1 if ans == float("inf") else ans

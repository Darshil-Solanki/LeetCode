class Solution:
    def maxScore(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n==1: return nums[0]*nums[0]
        def lcm(a,b):
            return a*b//gcd(a,b)
        def gcd(a,b):
            if b==0:
                return abs(a)
            return gcd(b, a%b)
        fwdLcm, fwdGcd = [0]*n, [0]*n
        fwdLcm[0] = fwdGcd[0] = nums[0]
        for i in range(1, n):
            fwdLcm[i]=lcm(fwdLcm[i-1], nums[i])
            fwdGcd[i]=gcd(fwdGcd[i-1], nums[i])
        bwdLcm, bwdGcd = [0]*n, [0]*n
        bwdLcm[-1] = bwdGcd[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            bwdLcm[i] = lcm(bwdLcm[i+1], nums[i])
            bwdGcd[i] = gcd(bwdGcd[i+1], nums[i])
        res = 0
        for i in range(n):
            if i == 0:
                res = max(res, bwdLcm[1]*bwdGcd[1])
            elif i == n-1:
                res = max(res, fwdLcm[i-1]*fwdGcd[i-1])
            else:
                res = max(res,
                    gcd(fwdGcd[i-1], bwdGcd[i+1])*
                    lcm(fwdLcm[i-1], bwdLcm[i+1]) )
        return max(res, fwdGcd[n-1]*bwdLcm[0])

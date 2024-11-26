class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        def mostPowerOfTwo(n):
            if n<=1:return 0
            return 1 << math.floor(math.log2(n))
        
        def allOnes(n):
            return (n & n-1)==0

        for n in nums:
            if n == 2:
                res.append(-1)
                continue
            tot, temp = 0, n
            while temp>0:
                t = mostPowerOfTwo(temp)
                if allOnes(temp+1):
                    tot+=temp//2
                    break
                tot+=t
                temp-=t
            res.append(tot)
        return res

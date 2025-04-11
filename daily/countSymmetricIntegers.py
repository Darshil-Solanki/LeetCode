class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        # count to two digit symmetric
        for n in range(11, 100, 11):
            if low<=n<=high:
                ans+=1

        #count of 4 digit symmetric
        if high>1000:
            for n in range(max(1001, low), min(high+1, 10000)):
                left = n//1000 + n%1000//100
                right = n%100//10 + n%10
                if left == right:
                    ans+=1
        return ans

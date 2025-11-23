class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        a = sum([x for x in nums if x%3==0]) # sum of 0 remainder
        b = sorted([x for x in nums if x%3==1], reverse=True) # 1 remainder
        c = sorted([x for x in nums if x%3==2], reverse=True)

        ans = 0
        len_b, len_c = len(b), len(c)
        for cntb in [len_b-2, len_b-1, len_b]:
            if cntb>=0:
                for cntc in [len_c-2, len_c-1, len_c]:
                    if cntc>=0 and (cntb -cntc)%3==0:
                        ans = max(ans, sum(b[:cntb]) + sum(c[:cntc]))
        
        return ans + a

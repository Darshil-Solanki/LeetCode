class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a_cnt = s.count("a")
        b_cnt = s.count("b")
        return abs(a_cnt-b_cnt)

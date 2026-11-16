class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            new_s = []
            for i in range(0, len(s), k):
                digit_sum_str = str(sum(map(int, s[i:i+k])))
                new_s.append(digit_sum_str)
            s = "".join(new_s)
        
        return s

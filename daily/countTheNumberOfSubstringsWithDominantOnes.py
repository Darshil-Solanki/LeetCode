class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pre_zero_i = [-1] * (n+1)
        
        for i in range(n):
            if i==0 or s[i-1]=="0":
                pre_zero_i[i+1] = i
            else:
                pre_zero_i[i+1] = pre_zero_i[i]
        
        ans = 0
        for i in range(1, n+1):
            zero_cnt = 1 if s[i-1] == "0" else 0
            j = i
            while j>0 and zero_cnt*zero_cnt <= i:
                one_cnt = (i-pre_zero_i[j]) - zero_cnt
                if zero_cnt*zero_cnt <= one_cnt:
                    ans += min(j - pre_zero_i[j], one_cnt - zero_cnt*zero_cnt + 1)
                
                j = pre_zero_i[j]
                zero_cnt +=1
        
        return ans

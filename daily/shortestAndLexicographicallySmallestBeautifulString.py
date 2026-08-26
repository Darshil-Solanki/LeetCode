class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1")<k:
            return ""

        left = cnt = 0
        ans = s
        for right, c in enumerate(s):
            cnt += int(c)
            
            while cnt>k or s[left]=="0":
                cnt -= int(s[left])
                left += 1
            
            if cnt == k:
                temp = s[left: right+1]
                if len(temp) < len(ans) or len(temp) == len(ans) and temp<ans:
                    ans = temp
        
        return ans

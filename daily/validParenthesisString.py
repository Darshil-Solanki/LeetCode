class Solution:
    def checkValidString(self, s: str) -> bool:
        open_cnt, close_cnt = 0, 0
        n = len(s)

        for i, c in enumerate(s):
            if c == "(" or c == "*":
                open_cnt += 1
            else:
                open_cnt -= 1
            
            if s[n-i-1] == ")" or s[n-i-1] == "*":
                close_cnt += 1
            else:
                close_cnt -= 1
            
            if open_cnt<0 or close_cnt<0:
                return False
        
        return True

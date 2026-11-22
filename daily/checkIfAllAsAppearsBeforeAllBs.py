class Solution:
    def checkString(self, s: str) -> bool:
        flag = False
        
        for c in s:
            if c == "b":
                flag = True
            else:
                if flag:
                    return False
        
        return True

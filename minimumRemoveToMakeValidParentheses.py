class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = close = 0
        ans = ""

        for c in s:
            if c=="(":
                ans+=c
                open+=1
            elif c==")":
                close+=1
                if open>=close:
                    ans+=c
                else:
                    close-=1
            else:
                ans+=c

        if open>close:
            ans = ans[::-1].replace("(", "", open-close)
            ans = ans[::-1]

        return ans        

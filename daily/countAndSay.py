class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        ans = "1"

        for i in range(2, n+1):
            curr = []
            count = 1
            
            for j in range(1, len(ans)):
                if ans[j]==ans[j-1]:
                    count+=1
                else:
                    curr.append(f"{count}{ans[j-1]}")
                    count=1
            
            curr.append(f"{count}{ans[-1]}")
            ans = "".join(curr)
        
        return ans

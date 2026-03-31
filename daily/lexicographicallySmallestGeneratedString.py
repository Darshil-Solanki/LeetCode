class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        ans = ["a"]*(n+m-1)
        fixed = [False]*(n+m-1)

        for i, c in enumerate(str1):
            if c == "T":
                for j in range(i, i+m):
                    if fixed[j] and ans[j]!=str2[j-i]:
                        return ""
                    ans[j], fixed[j] = str2[j-i], True
        
        for i, c in enumerate(str1):
            if c == "F":
                if any(str2[j - i] != ans[j] for j in range(i, i + m)):
                    continue
                for j in range(i+m-1, i-1, -1):
                    if not fixed[j]:
                        ans[j] = "b"
                        break
                else:
                    return ""
                
       
        return "".join(ans)

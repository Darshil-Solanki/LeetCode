class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = []

        for _ in range(m-1):
            ans.append("."+"#"*(n-1))
        
        ans.append("."*n)

        return ans

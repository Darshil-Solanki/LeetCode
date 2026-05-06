class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        ans = [["."]*m for _ in range(n)]

        for i in range(m):
            bottom_i = n-1
            for j in range(n-1, -1, -1):
                match boxGrid[i][j]:
                    case "#":
                        ans[bottom_i][m-i-1] = "#"
                        bottom_i -= 1
                    case "*":
                        ans[j][m-i-1] = "*"
                        bottom_i = j-1

        return ans

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        self.mat = mat

        def rotate():
            new = [[0]*n for _ in range(n)]
            flag=True
            for i in range(n):
                for j in range(n):
                    new[i][j] = self.mat[n-j-1][i]
                    if new[i][j] != target[i][j]:
                        flag = False
            self.mat = new
            return flag
        
        if mat==target:
            return True
        
        for i in range(3):
            if rotate():
                return True
        return False

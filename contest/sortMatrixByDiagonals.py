class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        if len(grid)==1: return grid
        tot_diagonal = len(grid)
        dec_diagonal = []
        for i in range(tot_diagonal):
            dec_diagonal.append([])
            j = 0
            temp = i
            while temp<tot_diagonal:
                dec_diagonal[-1].append(grid[temp][j])
                temp+=1
                j+=1
            dec_diagonal[-1].sort(reverse=True)
        inc_diagonal = []
        for j in range(1, tot_diagonal):
            inc_diagonal.append([])
            i=0
            temp = j
            while temp<tot_diagonal:
                inc_diagonal[-1].append(grid[i][temp])
                i+=1
                temp+=1
            inc_diagonal[-1].sort()
        
        for i, diagonal in enumerate(dec_diagonal):
            j = 0
            temp = i
            for num in diagonal:
                grid[temp][j]=num
                j+=1
                temp+=1
        for j, diagonal in enumerate(inc_diagonal):
            i = 0
            temp = j+1
            for num in diagonal:
                grid[i][temp]=num
                i+=1
                temp+=1
        return grid

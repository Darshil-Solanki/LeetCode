class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        tree = []
        h=len(triangle) # height of tree
        if h==1: return triangle[0][0]
        for i in range(h):
            for j in range(len(triangle[i])):
                tree.append(triangle[i][j])
        h-=1
        temp = 0
        for i in range(len(tree)-h-2, -1, -1):
            if temp==h:
                h-=1
                temp=0
            tree[i]=min(tree[i]+tree[i+h], tree[i]+tree[i+h+1])
            temp+=1
        return tree[0]

        # My earlier recursive solution
        # h = len(triangle)   # height of tree
        # if h==1: return triangle[0][0] 
        # def dp(i, j, res):
        #     left, right = triangle[i+1][j], triangle[i+1][j+1]
        #     if i==h-2:
        #         return min(res+left, res+right)
        #     if i==0:
        #         return min(dp(1, 0, res+triangle[1][0]), dp(1, 1, res+triangle[1][1]))
        #     return min(dp(i+1, j, res+left), dp(i+1, j+1, res+right))
        # return dp(0, 0, triangle[0][0])

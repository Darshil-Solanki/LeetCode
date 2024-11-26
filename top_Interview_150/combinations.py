class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(curr, i):
            if len(curr) == k:
                res.append(curr)
                return
            for j in range(i, n+1):
                temp = curr[:]
                temp.append(j)
                backtrack(temp,j+1)
        backtrack([], 1)
        return res
        
# using itertools combinations functions  
# if __name__ == '__main__':
#     with open('user.out','w') as f:
#         for n, k in zip(map(loads, stdin), map(loads, stdin)):
#             def combine(n: int, k: int) -> List[List[int]]:
#                 return combinations(range(1, n+1), k) 
#             print(json.dumps(tuple(combine(n, k))), file = f)
#     exit()

# proper use of backtrack template
# def combine(self, n: int, k: int) -> List[List[int]]:
#         def backtracking(start: int, length: int, tempcomb: List[int]):
#             if length == 0:
#                 ans.append(tempcomb[:])
#                 return
#             for num in range(start, n - length + 2):
#                 tempcomb.append(num)
#                 backtracking(num + 1, length - 1, tempcomb)
#                 tempcomb.pop()
#         ans = []
#         backtracking(1, k, [])
#         return ans

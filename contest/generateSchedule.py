class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n<5: return []

        ans = []
        if n%2: # odd
            for i in range(0, 2*n, 2):
                ans.append([i%n, (i+1)%n])
            for i in range(0, 2*n, 2):
                ans.append([(i+1)%n, i%n])
        else: # even
            for i in range(0, n, 2):
                ans.append([i, i+1])
            for i in range(0,  n, 2):
                ans.append([i+1, i])
            for i in range(1, n, 2):
                ans.append([i, (i+1)%n])
            for i in range(1, n, 2):
                ans.append([(i+1)%n, i])

        for diff in range(2, (n+1)//2):
            start = ans[-1][0] + 1
            for i in range(start, start+n):
                ans.append([i%n, (i+diff)%n])
            start = ans[-1][1] -1
            for i in range(start, start+n):
                ans.append([(i+diff)%n,i%n])
        
        if n%2 == 0:
            start = ans[-1][0]-1
            for i in range(start, start+n):
                ans.append([i%n, (i+n//2)%n])
        return ans

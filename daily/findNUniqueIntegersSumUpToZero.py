class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1: return [0]
        if n==2: return [-1, 1]
        if n==3: return [-1, 0, 1]

        ans = []
        if n%2==0:
            for i in range(1, (n//2)+1):
                ans.extend([i, -i])
            return ans
        i = 1
        while i<n//2:
            ans.extend([i, -i])
            i += 1

        ans.extend([-(i+i+1),i,i+1])
        return ans

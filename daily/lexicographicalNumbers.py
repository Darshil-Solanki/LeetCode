class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # result = []

        # def backtrack(curr):
        #     if curr>n: return
            
        #     for i in range(10):
        #         next = curr*10+i
        #         if 0<next<=n:
        #             result.append(next)
        #             backtrack(next) 
        
        # backtrack(0)
        # return result

        res = []
        curr = 1
        for _ in range(n):
            res.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                # backtrack
                if curr >= n:
                    curr //= 10
                curr += 1
                while curr % 10 == 0:
                    curr //= 10
        return res

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = 2*n-1
        result = [0]*length
        used = [False]*(n+1)

        def backtrack(pos):
            if pos == length:
                return True
            
            if result[pos]:
                return backtrack(pos+1)
            
            for i in range(n, 0, -1):
                if used[i]: continue

                if i==1:
                    result[pos]=1
                    used[1]=True
                    if backtrack(pos+1):
                        return True
                    result[pos]=0
                    used[1]=False
                else:
                    if pos+i<length and result[pos+i]==0:
                        result[pos]=i
                        result[pos+i]=i
                        used[i]=True
                        if backtrack(pos+1):
                            return True
                        result[pos]=0
                        result[pos+i]=0
                        used[i]=False
            return False
        
        backtrack(0)
        return result

        # use of set for used number
        # res = [0] * (2 * n - 1)
        # seen = set()
        # def backtrack(i):
        #     if i == len(res):
        #         return True
        #     if res[i]:
        #         return backtrack(i+1)
        #     for j in range(n,0,-1):
        #         if j in seen:
        #             continue
        #         seen.add(j)
        #         res[i] = j
        #         if j == 1:
        #             if backtrack(i+1):
        #                 return True
        #         elif j + i < len(res) and res[i+j] == 0:
        #             res[i+j] = j
        #             if backtrack(i+1):
        #                 return True
        #             res[i+j] = 0
        #         res[i] = 0
        #         seen.remove(j)
        #     return False
        # backtrack(0)
        # return res

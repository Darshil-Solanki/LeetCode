class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = {}
        n = len(candidates)
        def backtrack(curr, tot):
            if tot==target:
                copyCurr=curr[:]
                copyCurr.sort()
                sCurr = "".join(map(str,copyCurr))
                if sCurr not in comb:
                    res.append(copyCurr)
                    comb[sCurr]=1
                return
            if tot>target:
                return
            for n in candidates:
                curr.append(n)
                backtrack(curr, tot+n)
                curr.pop()
        
        backtrack([], 0)
        return res
    
        # Better version from submission
        # res = []
        # n = len(candidates)
        # candidates.sort()
        # def backtrack(curr, idx, rem):
        #     if rem==0:
        #         res.append(curr.copy())
        #         return
        #     for i in range(idx, n):
        #         if candidates[i]<=rem:
        #             curr.append(candidates[i])
        #             backtrack(curr, i, rem-candidates[i])
        #             curr.pop()
        #         else:
        #             return 
        # backtrack([], 0, target)
        # return res

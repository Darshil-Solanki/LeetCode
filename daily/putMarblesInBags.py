class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairWeights = [ weights[i]+weights[i+1] for i in range(n-1)]

        pairWeights.sort()
        ans = 0
        for i in range(k-1):
            ans += pairWeights[n-2-i]-pairWeights[i]
        
        return ans
    
    # same logic faster runtime
    # def putMarbles(self, weights: List[int], k: int) -> int:
    #     if k == 1:
    #         return 0 # min and max score are the same
        
    #     pairs = [ weights[i] + weights[i+1] for i in range(len(weights)-1) ]
    #     pairs.sort()

    #     max_score = sum(pairs[-(k-1):])
    #     min_score = sum(pairs[:k-1])

    #     return max_score - min_score

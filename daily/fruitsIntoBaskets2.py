class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        for f in fruits:
            for i in range(len(baskets)):
                if baskets[i]>=f:
                    baskets[i]=0
                    break
            else:
                ans+=1
        return ans

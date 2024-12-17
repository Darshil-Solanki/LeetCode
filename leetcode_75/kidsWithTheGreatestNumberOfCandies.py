class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        res = []
        for i, candy in enumerate(candies):
            res.append(candy+extraCandies>=mx)
        return res
        

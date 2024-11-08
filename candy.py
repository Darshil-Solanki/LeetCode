class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        res = [1]
        for i in range(1,len(ratings)):
            res.append( res[i-1]+1 if ratings[i]>ratings[i-1] else 1)
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i]>ratings[i+1] and res[i]<=res[i+1]:
                res[i]=res[i+1]+1
        return sum(res)

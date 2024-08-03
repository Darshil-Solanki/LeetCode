class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        temp = {}
        count = 0
        for p in pick:
            if temp.get(p[0]):
                if temp[p[0]].get(p[1]):
                    temp[p[0]][p[1]]+=1
                else:
                    temp[p[0]][p[1]]=1
            else:
                temp[p[0]]={p[1]:1}
        for i in temp:
            mx = max(temp[i].values())
            if mx>=i+1 :
                count+=1
        return count

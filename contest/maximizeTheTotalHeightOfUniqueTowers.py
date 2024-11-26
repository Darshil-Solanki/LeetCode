class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        tot = prev = maximumHeight[0]
        for i in range(1, len(maximumHeight)):
            curr_h = maximumHeight[i]
            if curr_h==prev:
                prev-=1
                if prev<1:
                    return -1
                tot+=prev
            elif curr_h<prev:
                prev = curr_h
                tot+=curr_h
            else:
                if prev>1:
                    prev-=1
                    tot+=prev
                else:
                    return -1
        return tot

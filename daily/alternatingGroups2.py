class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k-1])
        ans = 0
        left = 0

        for right in range(1, len(colors)):
            if colors[right]==colors[right-1]:
                left = right
            else:
                if right-left+1<k:
                    continue
                ans+=1
                left+=1

        return ans

        # faster runtime from submission
        # it is finding index where nearby color are same then calculating how many element is there in gap is making a group 
        # while this does perform more operation it still has 150 ms may be beacuse there are many cases that has 0 same color neighbour which make answer to n which run faster in below method
        # l = []
        # n = len(colors)
        # for i in range(n - 1):
        #     if colors[i] == colors[i + 1]:
        #         l.append(i)

        # if colors[n - 1] == colors[0]:
        #     l.append(n - 1)
        # if len(l) == 0:
        #     return n

        # l.append(l[0] + n)
        # res = 0
        # for i in range(len(l) - 1):
        #     res += max(0, l[i + 1] - l[i] - k + 1)

        # return res

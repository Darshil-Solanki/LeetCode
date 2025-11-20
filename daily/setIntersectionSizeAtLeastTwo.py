class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        todo = [2]*len(intervals)
        ans = 0
        
        while intervals:
            (s, e), t = intervals.pop(), todo.pop()
            for p in range(s, s+t):
                for i, (s0, e0) in enumerate(intervals):
                    if todo[i] and p<=e0:
                        todo[i] -= 1
                ans += 1
        
        return ans

        # faster approach
        # res, end1, end2 = 0, -1, -1
        # for s, e in sorted(intervals, key=lambda x:(x[1], -x[0])):
        #     if s <= end1:
        #         pass
        #     if end1 < s <= end2:
        #         res += 1
        #         end1, end2 = end2, e
        #     if s > end2:
        #         res += 2
        #         end1, end2 = e - 1, e
                
        # return res

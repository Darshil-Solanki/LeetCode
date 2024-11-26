class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for [curS, curE] in intervals:
            e=result[-1][1]
            if curS<=e:
                result[-1][1] =  curE if curE>e else e
            else:
                result.append([curS,curE])
        return result

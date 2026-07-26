class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        i = j = 0
        l1, l2 = len(series1), len(series2)
        ans = []
        while i < l1 and j < l2:
            if series1[i][0]<series2[j][0]:
                ans.append([series1[i][0], series1[i][1] + series2[j][1]])
                i += 1
            elif series1[i][0] == series2[j][0]:
                ans.append([series1[i][0], series1[i][1]+series2[j][1]])
                i += 1
                j += 1
            else:
                ans.append([series2[j][0], series1[i][1] + series2[j][1]])
                j += 1

        while i < l1:
            ans.append(series1[i])
            i += 1

        while j < l2:
            ans.append(series2[j])
            j += 1

        return ans

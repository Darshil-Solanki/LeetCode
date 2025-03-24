class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x: x[0])
        n = len(meetings)
        merged_meetings = [meetings[0]]
        ans = 0

        for i in range(1, n):
            prev = merged_meetings[-1]
            curr = meetings[i]
            if prev[1]>=curr[0]:
                if curr[1]>prev[1]:
                    merged_meetings[-1][1]=curr[1]
            else:
                ans += (curr[0]-prev[1]-1)
                merged_meetings.append(curr)
        
        if merged_meetings[-1][1]<days: ans+=(days-merged_meetings[-1][1])
        if merged_meetings[0][0]>1: ans+=(merged_meetings[0][0]-1)
        
        return ans

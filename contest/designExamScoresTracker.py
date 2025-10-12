class ExamTracker:

    def __init__(self):
        self.prefix_score = []
        self.tot = 0

    def record(self, time: int, score: int) -> None:
        self.tot += score
        self.prefix_score.append((time, self.tot))

    def totalScore(self, startTime: int, endTime: int) -> int:
        n = len(self.prefix_score)
        left, right = 0, len(self.prefix_score)-1
        while left<=right:
            mid = (left+right)//2
            if startTime>self.prefix_score[mid][0]:
                left = mid+1
            else:
                right = mid-1
        s_score = self.prefix_score[right][1] if right!=-1 else 0
       
        left, right = 0, len(self.prefix_score)-1
        while left<=right:
            mid = (left+right)//2
            if endTime>=self.prefix_score[mid][0]:
                left = mid+1
            else:
                right = mid-1
        e_score = self.prefix_score[right][1] if right!=-1 else 0 
        
        return e_score - s_score


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)

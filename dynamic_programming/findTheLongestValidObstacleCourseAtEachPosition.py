class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis, ans = [], []

        for obstacle in obstacles:
            pos = bisect_right(lis, obstacle)

            if pos==len(lis):
                lis.append(obstacle)
            else:
                lis[pos]=obstacle

            ans.append(pos+1)
        
        return ans

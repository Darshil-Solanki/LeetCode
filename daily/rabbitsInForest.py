class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        ans = 0

        # finding ratioo for each group and no of member can be
        for x_other, count in c.items():
            ans += ceil(count/(x_other+1))*(x_other+1)
        
        return ans

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        one, two, three = 0, 0, 0
        
        for i in range(1, n+1):
            t1 = three + costs[i-1] + 1
            t2 = (two + costs[i-1] if i>1 else float("inf")) + 4
            t3 = (one + costs[i-1] if i>2 else float("inf")) + 9
            temp = min(t1, t2, t3)
            one, two, three = two, three, temp

        return three

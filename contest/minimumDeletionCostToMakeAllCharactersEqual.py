class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        cost_of_c = defaultdict(int)

        for c, cst in zip(s, cost):
            cost_of_c[c] += cst
        
        max_cost_c = ("", 0)
        total = 0
        
        for c, tot in cost_of_c.items():
            if tot>max_cost_c[1]:
                max_cost_c = (c, tot)
            total += tot
            
        return total - max_cost_c[1]

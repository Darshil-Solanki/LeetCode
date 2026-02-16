class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1==0 and need2==0: return 0
        if need1==0:
            return min(cost2, costBoth)*need2
        if need2==0:
            return min(cost1, costBoth)*need1
        if (costBoth<cost1 and costBoth<cost2):
            return max(need1, need2)*costBoth
        if (costBoth<=cost1+cost2):
            min_pair, max_pair = min([need1, cost1], [need2, cost2]), max([need1, cost1], [need2, cost2])
            tot = min_pair[0]*costBoth
            max_pair[0] -= min_pair[0]
            if max_pair[1]<costBoth:
                return tot + max_pair[0]*max_pair[1]
            return tot + max_pair[0]*costBoth
        return need1*cost1 + need2*cost2
            
            

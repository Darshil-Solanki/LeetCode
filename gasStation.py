class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remainGas = []
        n= len(gas)
        for i,j in zip(gas,cost):
            remainGas.append(i-j)
        if sum(remainGas)<0:
            return -1
        total=0
        index =  0
        for i,val in enumerate(remainGas):
            total+=val
            if total<0:
                total=0
                index=i+1%n
        return index
    
    # Better way of doing same thing but using greedy style
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

    #     if sum(gas) < sum(cost):
    #         return -1
    #     total = 0
    #     start = 0
    #     for i in range(len(gas)):
    #         total += (gas[i] - cost[i])
    #         if total < 0:
    #             total = 0
    #             start = i+1

    #     return start
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     ## greedy
    #     ## time: O(n)
    #     ## space: O(1)

    #     total_gain = 0
    #     curr_gain = 0
    #     res = 0
        
    #     for i in range(len(gas)):
    #         total_gain += gas[i] - cost[i]
    #         curr_gain += gas[i] - cost[i]

    #         # If we meet a "valley", start over from the next station
    #         # with 0 initial gas.
    #         if curr_gain < 0:
    #             curr_gain = 0
    #             res = i + 1
        
    #     return res if total_gain >= 0 else -1

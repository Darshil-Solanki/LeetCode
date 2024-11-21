class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w>max(capital) and k>=len(profits):
            return sum(profits)+w
        maxProfit = []
        minCapital = list(zip(capital, profits))
        heapq.heapify(minCapital)
        for i in range(k):
            while minCapital and minCapital[0][0]<=w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p) # negating values for having maxheap using minheap
            if not maxProfit:
                break
            w += -heapq.heappop(maxProfit) # negating again to get actual values
        return w

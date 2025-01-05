class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        heapq.heapify(self.heap)
        self.seen = {key:True for key in range(1, 1001)}

    def popSmallest(self) -> int:
        n = heapq.heappop(self.heap)
        self.seen[n]=False
        return n

    def addBack(self, num: int) -> None:
        if not self.seen[num]:
            self.seen[num]=True
            heapq.heappush(self.heap, num)
    
    # More efficient version using min variable
    # def __init__(self):
    #     self.heap = []
    #     heapq.heapify(self.heap)
    #     self.set = set()
    #     self.min = 1
        
    # def popSmallest(self) -> int:
    #     if self.heap:
    #         elt = heapq.heappop(self.heap)
    #         self.set.remove(elt)
    #     else:
    #         elt = self.min
    #         self.min += 1
    #     return elt

    # def addBack(self, num: int) -> None:
    #     if num < self.min and num not in self.set:
    #         heapq.heappush(self.heap, num)
    #         self.set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

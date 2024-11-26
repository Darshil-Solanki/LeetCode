class MedianFinder:

    def __init__(self):
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        if self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            heapq.heappush(self.minHeap,-heapq.heappop(self.maxHeap))
        if len(self.maxHeap)-len(self.minHeap)>1:
            heapq.heappush(self.minHeap,-heapq.heappop(self.maxHeap))
        if len(self.minHeap)-len(self.maxHeap)>1:
            heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))



    def findMedian(self) -> float:
        mnLen, mxLen = len(self.minHeap), len(self.maxHeap)
        if mnLen==mxLen:
            return (self.minHeap[0]-self.maxHeap[0])/2
        if mnLen>mxLen:
            return self.minHeap[0]
        return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

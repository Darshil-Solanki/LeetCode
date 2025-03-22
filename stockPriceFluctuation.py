class StockPrice:

    def __init__(self):
        self.last = 0
        self.minheap = []
        self.maxheap = []
        self.records = {}
        

    def update(self, timestamp: int, price: int) -> None:
        self.records[timestamp] = price
        if timestamp>self.last: self.last = timestamp

        heappush(self.minheap, (price, timestamp))
        heappush(self.maxheap, (-price, timestamp))
        

    def current(self) -> int:
        return self.records[self.last]

    def maximum(self) -> int:
        maxprice, timestamp = heappop(self.maxheap)

        while -maxprice!=self.records[timestamp]:
            maxprice, timestamp = heappop(self.maxheap)

        heappush(self.maxheap, (maxprice, timestamp))
        return -maxprice

    def minimum(self) -> int:
        minprice, timestamp = heappop(self.minheap)

        while minprice!=self.records[timestamp]:
            minprice, timestamp = heappop(self.minheap)

        heappush(self.minheap, (minprice, timestamp))
        return minprice
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

class NumberContainers:

    def __init__(self):
        self.index = defaultdict(list)
        self.number = {}

    def change(self, index: int, number: int) -> None:
        self.number[index]=number
        heappush(self.index[number], index)
        

    def find(self, number: int) -> int:
        if number in self.index:
            while self.index[number]:
                idx = self.index[number][0]
                if self.number[idx]==number: return idx
                heappop(self.index[number]) 
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

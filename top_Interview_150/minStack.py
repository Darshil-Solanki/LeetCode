class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float("inf")        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.minimum,val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum = min(self.stack) if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum

    # Better way without use of min method(non O(1) complexity method) by using another copied stack 
    # def __init__(self):
    #     self.stack = []
    #     self.min_stack = []

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     self.min_stack.append(val if not self.min_stack or self.min_stack[-1] > val else self.min_stack[-1])

    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.min_stack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

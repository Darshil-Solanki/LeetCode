class DataStream:

    def __init__(self, value: int, k: int):
        #self.stream=[]
        self.n=0
        self.value=value
        self.k=k


    def consec(self, num: int) -> bool:
        #self.stream.append(True if(num==self.value) else False)
        #if(len(self.stream)<self.k):
            #return False
        #else:

   

            #return False not in self.stream[-self.k:]
        if(num==self.value):
            self.n+=1
        else:
            self.n=0
        return self.n>=self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
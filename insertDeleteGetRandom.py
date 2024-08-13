import random
class RandomizedSet:

    def __init__(self):
        self.items = set()

    def insert(self, val: int) -> bool:
        try:
            self.items.remove(val)
            self.items.add(val)
            return False
        except KeyError:
            self.items.add(val)
            return True

    def remove(self, val: int) -> bool:
        try:
            self.items.remove(val)
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        temp = tuple(self.items)
        return temp[random.randint(0,len(self.items)-1)]
        
    # Better Solutions with all O(1) complexity
    # def __init__(self):
    #     self.arr = []
    #     self.dic = {}
    #     self.set = set()   

    # def insert(self, val: int) -> bool:
    #     if val not in self.set:
    #         self.set.add(val)
    #         self.arr.append(val)
    #         self.dic[val] = len(self.arr)-1
    #         return True
    #     return False
        
    # def remove(self, val: int) -> bool:
    #     if val not in self.set:
    #         return False
    #     val_index = self.dic[val]
    #     last_el_in_list = self.arr[-1]
    #     index_of_last = self.dic[last_el_in_list]
        
    #     self.dic[val] = index_of_last
    #     self.dic[last_el_in_list] = val_index

    #     del(self.dic[val])
    #     self.arr[val_index],self.arr[index_of_last] = self.arr[index_of_last],self.arr[val_index]
    #     self.arr.pop()

    #     self.set.remove(val)
    #     return True
    # def getRandom(self) -> int:
    #     return self.arr[random.randint(0,len(self.items)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

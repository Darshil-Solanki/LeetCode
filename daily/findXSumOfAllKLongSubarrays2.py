class Helper:
    def __init__(self, x):
        self.x, self.result = x, 0
        self.large, self.small, self.cnt = SortedList(), SortedList(),Counter()
    
    def get(self,):
        return self.result

    def insert(self, num):
        if self.cnt[num]>0:
            self._remove((self.cnt[num], num))
        self.cnt[num] += 1
        self._insert((self.cnt[num], num))
    
    def _insert(self, t):
        if len(self.large)<self.x or t>self.large[0]:
            self.result += t[0]*t[1]
            self.large.add(t)
            if len(self.large)>self.x:
                to_remove = self.large[0]
                self.result -= to_remove[0]*to_remove[1]
                self.large.remove(to_remove)
                self.small.add(to_remove)
        else:
            self.small.add(t)
    
    def remove(self, num):
        self._remove((self.cnt[num], num))
        self.cnt[num] -= 1
        if self.cnt[num]>0:
            self._insert((self.cnt[num], num))
    
    def _remove(self, t):
        if t>=self.large[0]:
            self.result -= t[0]*t[1]
            self.large.remove(t)
            if self.small:
                to_add = self.small[-1]
                self.result += to_add[0]*to_add[1]
                self.small.remove(to_add)
                self.large.add(to_add)
        else:
            self.small.remove(t)


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        h = Helper(x)
        
        for i in range(n):
            h.insert(nums[i])
            if i>=k:
                h.remove(nums[i-k])
            if i>=k-1:
                ans.append(h.get())
        
        return ans
            

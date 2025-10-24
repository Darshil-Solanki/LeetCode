class Solution:
    def balanced_num(self, num):
        cnt = Counter(str(num))
        for c, count in cnt.items():
            if ord(c) - 48 != count:
                return False
        return True
        
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1, 1224445):
            if self.balanced_num(i):
                return i

class BIT:
    def __init__(self, n: int):
        self.size = n
        self._tree1 = defaultdict(int)
        self._tree2 = defaultdict(int)
    
    def _lowbit(self, index: int) -> int:
        return index & -index
    
    def add(self, left: int, right: int, delta: int) -> None:
        self._add(left, delta)
        self._add(right+1, -delta)
    
    def query(self, left: int, right: int) -> int:
        return self._query(right) - self._query(left - 1)
    
    def _add(self, index: int, delta: int) -> None:
        index += 1
        raw_index = index
        while index <= self.size:
            self._tree1[index] += delta
            self._tree2[index] += (raw_index - 1) * delta
            index += self._lowbit(index)

    def _query(self, index: int) -> int:
        index += 1
        if index > self.size:
            index = self.size
        
        raw_index = index
        ans = 0
        while index > 0:
            ans += raw_index * self._tree1[index] - self._tree2[index]
            index -= self._lowbit(index)
        
        return ans


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = curr = 0
        bit = BIT(n + 10)
        seen = {}
        MOD = 1_000_000_007
        
        for i, num in enumerate(nums):
            j = seen.get(num, -1) + 1
            curr = (curr + bit.query(j, i) * 2 + i -j + 1) % MOD
            ans = (ans + curr) % MOD
            bit.add(j, i, 1)
            seen[num] = i
        
        return ans

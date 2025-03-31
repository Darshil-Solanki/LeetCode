class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        result = []
        temp = [(num, freq) for num, freq in c.items()]
        temp.sort(key = lambda x: (x[1], -x[0]))
        return [num for num, freq in temp for _ in range(freq)]

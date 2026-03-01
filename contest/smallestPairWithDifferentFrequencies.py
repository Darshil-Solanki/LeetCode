class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        temp = []
        for x, xf in cnt.items():
            for y, yf in cnt.items():
                if x!=y and x<y and xf!=yf:
                    temp.append((x, y))

        temp.sort()
        return temp[0] if temp else [-1, -1]

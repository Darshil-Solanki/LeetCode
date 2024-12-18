class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n: return True
        prev = flowerbed[0]
        tot, length = 0, len(flowerbed)
        for i, curr in enumerate(flowerbed):
            next = flowerbed[i+1] if i+1<length else 0
            if not prev and not curr and not next:
                tot+=1
                prev = 1
                continue
            prev = curr
        return tot>=n

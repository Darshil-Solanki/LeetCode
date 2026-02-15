class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        map = defaultdict(bool)
        for b in bulbs:
            map[b] = not map[b]
        return list(sorted(b for b, status in map.items() if status))

class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        heap = []
        cx, cy = center
        for x, y, q in towers:
            dist = abs(cx-x)+abs(cy-y)
            if dist<=radius:
                heap.append((-q, x, y))

        if not heap:
            return [-1, -1]
        heapify(heap)
        q, x, y = heappop(heap)
        return [x, y]

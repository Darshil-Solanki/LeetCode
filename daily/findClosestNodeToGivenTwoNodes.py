class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        distance_from1 = [float("inf")]*n
        distance_from1[node1] = 0
        distance_from2 = [float("inf")]*n
        distance_from2[node2] = 0
        heap = [(0, node1)]

        while heap:
            curr_dist, node = heappop(heap)
            if curr_dist>distance_from1[node]: continue
            nei = edges[node]
            if nei != -1 and curr_dist+1<distance_from1[nei]:
                distance_from1[nei] = curr_dist + 1
                heappush(heap, (curr_dist+1, nei))
        
        heap = [(0, node2)]
        ans_heap = []
        while heap:
            curr_dist, node = heappop(heap)
            if curr_dist>distance_from2[node]: continue
            if distance_from1[node]!=float("inf"):
                heappush(ans_heap, (max(distance_from1[node], distance_from2[node]) , node))
            nei = edges[node]
            if nei != -1 and curr_dist + 1 <distance_from2[nei]:
                distance_from2[nei] = curr_dist + 1
                heappush(heap, (curr_dist+1, nei))
        
        return -1 if not ans_heap else heappop(ans_heap)[1]

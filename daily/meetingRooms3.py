class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free_room_heap = list(range(n))
        used_room_heap = []
        heapify(free_room_heap)
        meeting_count = [0]*n
        meetings.sort()

        for start, end in meetings:
            while used_room_heap and used_room_heap[0][0]<=start:
                _, room = heappop(used_room_heap)
                heappush(free_room_heap, room)

            if free_room_heap:
                room = heappop(free_room_heap)
                heappush(used_room_heap, (end, room))
            else:
                end_time, room = heappop(used_room_heap)
                heappush(used_room_heap, (end_time + end - start, room))
            
            meeting_count[room] += 1
        
        return meeting_count.index(max(meeting_count))

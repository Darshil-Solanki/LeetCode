class EventManager:

    def __init__(self, events: list[list[int]]):
        self.heap = [(-p, e) for e, p in events]
        heapify(self.heap)
        self.event_pri = {}
        for e, p in events:
            self.event_pri[e] = -p

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.event_pri[eventId] = -newPriority
        heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.heap:
            p, e = heappop(self.heap)
            if self.event_pri.get(e, None)==p:
                del self.event_pri[e]
                return e
        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()

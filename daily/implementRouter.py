class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.packet_queue = deque([])
        self.packets = defaultdict(bool)
        self.destination_to_time = defaultdict(list)
              
    def getPacketStr(self, s, d, t):
        return str(s)+"-"+str(d)+"-"+str(t)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet_str = self.getPacketStr(source, destination, timestamp)
        if packet_str in self.packets:
            return False
        if len(self.packet_queue)==self.limit:
            s, d, t = self.packet_queue.popleft()
            r_packet_str = self.getPacketStr(s, d, t)
            del self.packets[r_packet_str]
            self.destination_to_time[d].remove(t)
        
        self.packet_queue.append((source, destination, timestamp))
        self.packets[packet_str] = True
        self.destination_to_time[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packet_queue:
            return []
        s, d, t = self.packet_queue.popleft()
        r_packet_str = self.getPacketStr(s, d, t)
        del self.packets[r_packet_str]
        self.destination_to_time[d].remove(t)
        return [s, d, t]
              
    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        length = len(self.destination_to_time[destination])
        left = bisect_left(self.destination_to_time[destination], startTime)
        if left == length:
            return 0
        right = bisect_right(self.destination_to_time[destination], endTime)
        return right-left
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)

class RideSharingSystem:

    def __init__(self):
        self.riders = defaultdict(bool)
        self.rider_to_driver = defaultdict(int)
        self.rider_queue = deque([])
        self.driver_queue = deque([])

    def addRider(self, riderId: int) -> None:
        self.riders[riderId] = True
        self.rider_queue.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.driver_queue.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if self.rider_queue and self.driver_queue:
            r, d = self.rider_queue.popleft(), self.driver_queue.popleft()
            self.rider_to_driver[r] = d
            return [d, r]
        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riders and riderId not in self.rider_to_driver:
            try:
                self.rider_queue.remove(riderId)
            except:
                pass


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)

class BusBooking:

    def __init__(self, n: int):
        self.rows = [[0]*4 for _ in range(n+1)]
        self.min_time = 0
        self.total_time = 0

    def toggle(self, seat: str) -> None:
        col, row = seat[0], seat[1:]
        col, row = ord(col)-65, int(row) if row else 0
        if self.rows[row][col]: # already booked
            self.min_time -= 1
            self.total_time -= self.rows[row][col]
            self.rows[row][col] = 0
        else:
            self.rows[row][col] = self.get_cost(row, col)    
            self.total_time += self.rows[row][col]
            self.min_time += 1


    def get_cost(self, row, col):
        if col in (1, 2):
            return 1
        if col == 0 and self.rows[row][1]:
                return 3
        if col == 3 and self.rows[row][2]:
                return 3
        return 1
                

    def getTotalTime(self) -> int:
        return self.total_time

    def getMinTime(self) -> int:
        return self.min_time


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()

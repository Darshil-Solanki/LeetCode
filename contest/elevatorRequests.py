class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        elevator = 0
        ans = 0
        
        for req in requests:
            ans += abs(elevator-req)
            elevator = req

        return ans

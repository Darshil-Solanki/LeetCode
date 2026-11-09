class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        request_handled = [0] * k
        busy_server = []
        free_server = list(range(k))

        for i, (arrival_time, need_time) in enumerate(zip(arrival, load)):
            while busy_server and busy_server[0][0] <= arrival_time:
                _, server_i= heappop(busy_server)
                heappush(free_server, i + (server_i - i) % k)

            if free_server:
                server_i = heappop(free_server) % k
                request_handled[server_i] += 1
                heappush(busy_server, (arrival_time+need_time, server_i))

        curr_max = 0
        ans = []
        for i, req_h in enumerate(request_handled):
            if req_h>curr_max:
                ans = [i]
                curr_max = req_h
            elif req_h == curr_max:
                ans.append(i)
        
        return ans

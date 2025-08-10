class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        ele = [(limit[i], value[i], i) for i in range(len(value))]
        ele.sort(key = lambda x: (x[0], -x[1], x[2]))

        ele = deque(ele)
        active = deque([])
        tot = 0
        while ele:
            limit, val, original_idx = ele.popleft() 
            if len(active)<limit:
                active.append(limit)
                tot += val
                activated = len(active)
                while active and active[0]<=activated:
                    active.popleft()
                while ele and ele[0][0]<=activated:
                    ele.popleft()
        
        return tot

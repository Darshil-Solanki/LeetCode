class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1]*len(rains)
        sl = SortedList()
        last_rain_day = defaultdict(int)

        for i, rl in enumerate(rains):
            if not rl:
                sl.add(i)
            else:
                ans[i] = -1
                if rl in last_rain_day:
                    sl_i = sl.bisect(last_rain_day[rl])
                    if sl_i == len(sl):
                        return []
                    ans[sl[sl_i]] = rl
                    sl.discard(sl[sl_i])    
                last_rain_day[rl] = i
        
        return ans

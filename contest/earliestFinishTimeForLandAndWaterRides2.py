class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        landRides = list(zip(landStartTime, landDuration))
        waterRides = list(zip(waterStartTime, waterDuration))
        landRides.sort(key = lambda x: sum(x))
        waterRides.sort(key = lambda x: sum(x))
        
        ans1, ans2 = float("inf"), float("inf")
        time1 = time2 = 0
        time1 = sum(landRides[0])
        for w_start, w_dur in waterRides:
            if w_start<=time1:
                ans1 = min(ans1, time1+w_dur)
            else:
                ans1 = min(ans1, w_start+w_dur)
                break
        
        time2 = sum(waterRides[0])
        for l_start, l_dur in landRides:
            if l_start<=time2:
                ans2 = min(ans2, time2+l_dur)
            else:
                ans2 = min(ans2, l_start+l_dur)

        return min(ans1, ans2)

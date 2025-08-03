class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        landRides = list(zip(landStartTime, landDuration))
        waterRides = list(zip(waterStartTime, waterDuration))

        ans = float("inf")
        for i, l_ride in enumerate(landRides):
            for j, w_ride in enumerate(waterRides):
                time1 = time2 = 0
                time1 = sum(l_ride)
                if time1<w_ride[0]:
                    time1 = sum(w_ride)
                else:
                    time1 += w_ride[1]

                time2 = sum(w_ride)
                if time2<l_ride[0]:
                    time2 = sum(l_ride)
                else:
                    time2 += l_ride[1]
                    
                ans = min(ans, time1, time2)

        return ans

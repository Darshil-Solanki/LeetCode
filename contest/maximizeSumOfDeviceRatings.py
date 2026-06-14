class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        m, n = len(units), len(units[0])
        lowest = float("inf")
        min_sum = 0
        min_max = float("inf")

        for device in units:
            if len(device) == 1:
                min1 = device[0]
                min2 = 0
            else:
                min1 = min(device)
                device.remove(min1)
                min2 = min(device)
            
            if min1 < lowest:
                lowest = min1
            
            mx = max(min1, min2)
            min_sum += mx

            if mx<min_max:
                min_max = mx
        
        return min_sum + lowest - min_max

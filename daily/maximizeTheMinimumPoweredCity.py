class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        def check(power) -> bool:
            diff = diff_arr.copy()
            total = 0
            remaining = k

            for i in range(n):
                total += diff[i]
                if total < power:
                    add = power - total
                    if remaining < add:
                        return False
                    remaining -= add
                    end = min(n, i + 2*r + 1)
                    diff[end] -= add
                    total += add

            return True

        n = len(stations)
        diff_arr = [0]*(n+1)
        for i in range(n):
            left = max(0, i-r)
            right = min(n, i+r+1)
            diff_arr[left] += stations[i]
            diff_arr[right] -= stations[i]


        left, right = min(stations), sum(stations) + k
        ans = 0
        while left <= right:
            mid = (left+right)//2
            if check(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1

        return ans 

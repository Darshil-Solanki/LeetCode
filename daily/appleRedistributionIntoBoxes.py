class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        tot_apples = sum(apple)
        ans = 0
        for cap in capacity:
            tot_apples -= cap
            ans += 1
            if tot_apples<1:
                return ans

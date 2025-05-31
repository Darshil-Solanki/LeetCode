class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        def get_cost(a_list, b_list):
            ans = 0
            
            for a, b in zip(a_list, b_list):
                ans += abs(a-b)

            return ans

        return min(get_cost(arr, brr), get_cost(sorted(arr), sorted(brr))+k ) 

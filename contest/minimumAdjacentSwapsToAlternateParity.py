class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        even_indices, odd_indices = [], []
        n = len(nums)
        for i, num in enumerate(nums):
            if num%2: # odd
                odd_indices.append(i)
            else:
                even_indices.append(i)
        
        odd, even = len(odd_indices), len(even_indices)
        if abs(odd-even)>1: return -1

        def calc_swap(is_odd_first):
            ans = 0
            i = 0

            if is_odd_first:
                for odd_idx in odd_indices:
                    ans += abs(odd_idx-i)
                    i += 2
            else:
                for even_idx in even_indices:
                    ans += abs(even_idx-i)
                    i += 2

            return ans

        ans = float("inf")
        if odd>even:
            ans = min(ans, calc_swap(1))
        elif even>odd:
            ans = min(ans, calc_swap(0))
        else:
            odd_swap = calc_swap(1)
            even_swap = calc_swap(0)
            ans = min(ans, odd_swap, even_swap)
        
        return ans

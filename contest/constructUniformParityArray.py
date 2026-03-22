class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd_count, even_count = 0, 0
        for num in nums1:
            if num%2:
                odd_count += 1
            else:
                even_count += 1
        if odd_count > 1:
            return True
        if even_count>=1 and odd_count>=1:
            return True
        if (odd_count == 0 and even_count) or (even_count ==0 and odd_count):
            return True

        return False
        

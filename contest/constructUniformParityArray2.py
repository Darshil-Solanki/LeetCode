class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_even, min_odd = float("inf"), float("inf")
        for num in nums1:
            if num%2:
                min_odd = min(min_odd, num)
            else:
                min_even = min(min_even, num)

        if (min_even!=float("inf") and min_odd==float("inf")) or (min_even==float("inf") and min_odd!=float("inf")):
            return True
            
        # making even
        even_flag = True
        for num in nums1:
            if num%2:
                if num==min_odd or num-min_odd<1:
                    even_flag = False

        if even_flag:
            return True

        # making odd
        for num in nums1:
            if num%2==0:
                if num-min_odd <1:
                    return False
        return True
        
        # from submission best solutoins
        # small=min(nums1)
        # if small%2==1:
        #     return True
        # for num in nums1:
        #     if num%2==1:
        #         return False
        # return True
        
                

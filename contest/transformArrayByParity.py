class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even = odd = 0
        for n in nums:
            if n%2:
                odd+=1
            else:
                even+=1
        return [0]*even + [1]*odd
    
    # better version
    # def transformArray(self, nums: List[int]) -> List[int]:
    #     return sorted([0 if i % 2 == 0 else 1 for i in nums])

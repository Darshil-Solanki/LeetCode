class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        unpaired = set()

        for num in nums:
            if num in unpaired:
                unpaired.remove(num)
            else:
                unpaired.add(num)
        
        return len(unpaired)==0

        # counter=collections.Counter(nums)
        # for count in counter.values():
        #     if count%2: # if odd
        #         return False
        
        # return True

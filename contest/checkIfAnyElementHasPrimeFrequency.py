class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        prime_set = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        
        for val in cnt.values():
            if val in prime_set: return True
                
        return False

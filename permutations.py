class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(curr, numList):
            if len(nums)==len(curr):
                res.append(curr[:])
                return
            
            for i in range(len(numList)):
                newNumList = numList[:i]+numList[i+1:]
                curr.append(numList[i])
                backtrack(curr, newNumList)
                curr.pop()         
        
        backtrack([], nums)
        return res
    
    # Better Performance code
    # def p(self , nums , tmp , store ) :
    #     if not nums :
    #         store.append(list(tmp))
    #         return
    #     for i in range(len(nums)) :
    #         tmp.append(nums[i])
    #         poped = nums.pop(i)
    #         self.p( nums , tmp , store)
    #         nums.insert(i , poped)
    #         tmp.remove(poped)

    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     store = []
    #     self.p(nums , [] , store)
    #     return store
        

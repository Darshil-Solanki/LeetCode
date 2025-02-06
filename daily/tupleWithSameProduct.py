class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums)<4: return 0
        ans = 0
        product_dict = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product_dict[nums[i]*nums[j]]+=1
        for value in product_dict.values():
            if value>1:
                ans+= value*(value-1)*4
        return ans

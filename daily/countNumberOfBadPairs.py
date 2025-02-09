class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        max_pair = n*(n-1)//2
        map = defaultdict(int)
        ans = 0
        for i, n in enumerate(nums):
            ans+=map[i-n]
            map[i-n]+=1
        return max_pair-ans

        # fastest method
        # n = len(nums)
        # nums_new = [ num - i for i, num in enumerate(nums)]
        # count = Counter(nums_new)
        # total_pairs = n*(n-1)//2 

        # for key, val in count.items(): 
        #     if val!=1: 
        #         total_pairs -= val*(val-1)//2

        # return total_pairs

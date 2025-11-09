class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        
        for i, num in enumerate(nums):
            indices[num].append(i)
            
        ans = float("inf")
        for num, ind_list in indices.items():
            if len(ind_list)>2:
                for i in range(1, len(ind_list)-1):
                    left, right = ind_list[i-1], ind_list[i+1]
                    ans = min(ans, 2*(right-left))

        return -1 if ans==float("inf") else ans

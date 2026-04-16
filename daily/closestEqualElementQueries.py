class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        num_idx = defaultdict(list)
        for i, num in enumerate(nums):
            num_idx[num].append(i)
        
        ans = [-1]*len(queries)
        for i, q in enumerate(queries):
            if len(num_idx[nums[q]])<2:
                continue
            temp = float("inf")
            indices = num_idx[nums[q]]
            left = bisect_left(indices, q)
            right = bisect_right(indices, q)
            if indices[left] != q:
                temp = min(temp, abs(q-indices[left]), q+n-indices[left], n-q+indices[left])
            if indices[left] == q:
                if left>0:
                    left -= 1
                else:
                    left = -1
                temp = min(temp, abs(q-indices[left]), q+n-indices[left], n-q+indices[left])
            if right!=len(indices) and indices[right] != q:
                temp = min(temp, abs(q-indices[right]), q+n-indices[right], n-q+indices[right])
            if right == len(indices):
                temp = min(temp, abs(q-indices[0]), q+n-indices[0], n-q+indices[0])
            
            if temp != float("inf"):
                ans[i] = temp
        
        return ans

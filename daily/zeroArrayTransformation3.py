class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        n = len(nums)
        heap = []
        diff_arr = [0]*(n+1)
        j = prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += diff_arr[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            while prefix_sum < num and heap and -heap[0] >= i:
                prefix_sum += 1
                diff_arr[-heappop(heap)+1] -= 1
            
            if prefix_sum < num: return -1  

        return len(heap)

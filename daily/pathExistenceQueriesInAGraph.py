class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component_no = 0
        components = [0]*n
        ans = []
        for i in range(1, n):
            if (nums[i]-nums[i-1]) > maxDiff:
                component_no += 1
            components[i] = component_no
        
        for l, r in queries:
            ans.append(components[l] == components[r])
        
        return ans

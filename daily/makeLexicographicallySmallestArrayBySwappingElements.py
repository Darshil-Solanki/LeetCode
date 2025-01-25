class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        if not nums: return []
        n = len(nums)
        sorted_pairs = sorted([(n, i) for i, n in enumerate(nums)])
        result = [0]*n
        group_start = 0
        for i in range(n):
            if i==n-1 or sorted_pairs[i+1][0]-sorted_pairs[i][0] > limit:
                indices = [pair[1] for pair in sorted_pairs[group_start:i+1]]
                indices.sort()
                for j, idx in enumerate(indices):
                    result[idx] = sorted_pairs[group_start+j][0]
                group_start = i+1
        return result

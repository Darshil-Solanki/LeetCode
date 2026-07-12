class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_num = sorted(set(arr))
        rank = {num:i for i, num in enumerate(sorted_num, 1)}
        return [rank[num] for num in arr]

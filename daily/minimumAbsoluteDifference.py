class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")
        
        for i in range(len(arr)-1):
            min_diff = min(min_diff, arr[i+1]-arr[i])
        
        res = []
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] == min_diff:
                res.append([arr[i], arr[i+1]])
        
        return res

    # Same logic but combined both loop with creating pair list on the go
    # def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
    #     ans = []
    #     mn = math.inf

    #     arr.sort()

    #     for a, b in itertools.pairwise(arr):
    #         diff = b - a
    #         if diff < mn:
    #             mn = diff
    #             ans = []
    #         if diff == mn:
    #             ans.append([a, b])

    #     return ans

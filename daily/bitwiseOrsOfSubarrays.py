class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        num_set = set(arr)
        curr = {0}

        for num in arr:
            curr = {num|num2 for num2 in curr} | {num}
            num_set |= curr

        return len(num_set)
        
        # num_set = set(arr)
        # n = len(arr)

        # for i, num in enumerate(arr):
        #     bor = num
        #     for j in range(i+1, n):
        #         bor = bor|arr[j]
        #         num_set.add(bor)

        # return len(num_set)

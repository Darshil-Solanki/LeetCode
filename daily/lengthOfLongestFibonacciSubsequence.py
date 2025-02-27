class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        arrSet = set(arr)
        max_len = 0

        for i in range(n):
            for j in range(i+1, n):
                prev, curr = arr[i], arr[j]
                curr_len = 2

                while prev+curr in arrSet:
                    prev, curr = curr, prev+curr
                    curr_len+=1

                if curr_len>max_len:
                    max_len = curr_len

        return max_len if max_len>2 else 0

        # faster version from submission using dictionary instead of set
        # lookup = {}
        # res = 0
        # for pos, num in enumerate(arr):
        #     lookup[num] = defaultdict(lambda: 2)
        #     for prev_pos in range(pos - 1, -1, -1):
        #         prev = arr[prev_pos]
        #         prev2 = num - prev
        #         if prev2 >= prev:
        #             break
        #         if prev2 not in lookup:
        #             continue
        #         lookup[num][prev] = lookup[prev][prev2] + 1
        #         res = max(res, lookup[num][prev])
        # return res

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1_000_000_007
        ans = curr = 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        for n in arr:
            curr+=n
            if curr%2:
                ans+=prefixSum[0]
            else:
                ans+=prefixSum[1]
            prefixSum[curr%2]+=1

        return ans%MOD

        # faster and memory efficient method
        # cumSum = odd = even = 0
        # for num in arr:
        #     cumSum += num
        #     if cumSum % 2:
        #         odd += 1
        #     else:
        #         even += 1
        # return odd * (even + 1) % (pow(10, 9) + 7)

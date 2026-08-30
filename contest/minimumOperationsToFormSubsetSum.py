class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        dp = [float("inf")]*(sum+1)
        dp[0] = 0
        for x in nums:
            choices = {}

            if not x:
                choices[0] = 0
            else:
                value = x
                operations = 0
                while value>0:
                    if value <= sum:
                        choices[value] = min(choices.get(value, float("inf")), operations)
                    value //= 2
                    operations += 1

                choices[0] = min(choices.get(0, float("inf")), operations)

                value = x
                operations = 0
                while value<=sum:
                    choices[value] = min(choices.get(value, float("inf")), operations)
                    if value > sum//2:
                        break
                    value *= 2
                    operations +=1
            
            new_dp = dp[:]
            for curr in range(sum+1):
                if dp[curr] == float("inf"):
                    continue
                for value, cost in choices.items():
                    next_sum = curr + value
                    if next_sum <= sum:
                        new_dp[next_sum] = min(new_dp[next_sum], dp[curr]+cost)

            dp = new_dp

        return -1 if dp[sum]==float("inf") else dp[sum]

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        cnt = n
        pre = [0]*(2*n+1)
        pre[n] = 1
        presum = 0

        for num in nums:
            if num==target:
                presum += pre[cnt]
                cnt += 1
            else:
                cnt -= 1
                presum -= pre[cnt]
            pre[cnt] += 1
            ans += presum
        
        return ans

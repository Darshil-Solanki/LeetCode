class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = defaultdict(int)
        count[0] = 1

        ans = 0
        prefix = 0 # count for nums[i]%mod till ith index

        for num in nums:
            prefix += 1 if num%modulo == k else 0
            ans += count[(prefix - k) % modulo]
            count[ prefix % modulo] += 1
        
        return ans

        # from editorial
        # updated version with better understandable calculation
        # Since we need to count the number of occurrences of special elements in the array interval, we can consider using prefix sums.
        # We define sum[i] as the number of special elements that satisfy x mod modulo=k in the array nums from index 0 to i.
        # The number of special elements in the subarray nums[l..r] is then sum[r]−sum[l−1].
        # According to the description, it can be deduced that at this time, in order to satisfy intersting subarray condition:

        # (sum[r]−sum[l−1]) mod modulo=k
        # (sum[r]-sum[l-1]+modulo) mod modulo = (k+modulo) mod modulo  because (a+b)%b will be a%b as b will cancel out in remainder
        # subtract k and add sum[l-1] to both side will not effect modulo because both side are added and subtracted equal value it doesn't change modulo   (a+d)%b (c+d)%b
        # (sum[r] - k + modulo) mod modulo = (sum[l-1]+modulo) mod modulo
        # (sum[r] - k) mod modulo = sum[l-1] mod modulo because (a+b)%b = a%b



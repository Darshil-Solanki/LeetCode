class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapify(nums)
        if nums[0]>=k: return 0
        while nums[0]<k:
            a, b = heappop(nums), heappop(nums)
            heappush(nums, a*2+b)
            ans+=1
        return ans

        # faster runtime than heap method
        # non heap method using sorting and finding and updating first two minimum
        # nums.sort()
        # n = len(nums)
        # ret = 0
        # i = 0
        # temp = []
        # j = 0
        # size = 0
        # while (n-i + size-j) >= 2:
        #     if i < n:
        #         first = nums[i]
        #         if j < size and temp[j] < first:
        #             first = temp[j]
        #             j += 1
        #         else:
        #             i += 1
        #     else:
        #         first = temp[j]
        #         j += 1
        #     if first >= k:
        #         break
        #     if i < n:
        #         second = nums[i]
        #         if j < size and temp[j] < second:
        #             second = temp[j]
        #             j += 1
        #         else:
        #             i += 1
        #     else:
        #         second = temp[j]
        #         j += 1
        #     new = (min(first, second)*2) + max(first, second)
        #     size += 1
        #     ret += 1
        #     temp.append(new)
        # return ret

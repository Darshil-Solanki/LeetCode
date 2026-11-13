class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        # copied from editorial
        n = len(nums)
        ans = 0
        operations = 0

        queue = []
        cnt = [[] for _ in range(n)]
        pos = [n] * n
        stack = []

        left = 0
        for right, num in enumerate(nums):
            while stack and num >= nums[stack[-1]]:
                pos[stack[-1]] = right
                stack.pop()
            
            if stack:
                cnt[stack[-1]].append(right)
            stack.append(right)

            heappush(queue, (-num, right))
            operations += max(0, -queue[0][0] - num)

            while operations > k:
                for i in cnt[left]:
                    operations -= (nums[left] - nums[i]) * ( min(pos[i], right+1) - i )
                
                left += 1
            
            while queue and queue[0][1] < left:
                heappop(queue)

            ans += right - left + 1

        return ans

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        duplicates = defaultdict(int)
        for num, count in cnt.items():
            if count>1:
                duplicates[num]=count
        if not duplicates:
            return 0
            
        queue = Deque(nums)
        ans = 0
        for _ in range(len(nums)//3):
            for i in range(3):
                num = queue.popleft()
                cnt[num] -= 1
                if cnt[num] == 0:
                    del cnt[num]
                if num in duplicates:
                    duplicates[num] -= 1
                    if duplicates[num] == 1:
                        del duplicates[num]
            ans += 1
            if not duplicates:
                return ans
        return ans+1

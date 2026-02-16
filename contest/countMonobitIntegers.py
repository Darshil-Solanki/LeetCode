class Solution:
    def countMonobit(self, n: int) -> int:
        ans = 1
        def all_one(num):
            return len(bin(num))-2 == bin(num).count("1")
            
        for i in range(1, n+1):
            if all_one(i):
                ans += 1
        return ans

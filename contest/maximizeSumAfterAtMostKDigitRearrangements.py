class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        temp = []

        def get_max_num(num):
            return int("".join(list(sorted(str(num), key = lambda x: -int(x)))))
        
        for num in nums:
            mx_num = get_max_num(num)
            temp.append((mx_num-num, num))

        temp.sort(key = lambda x: -x[0])

        ans = sum(nums)
        for i in range(k):
            ans += temp[i][0]

        return ans      

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans |= num

        nums.sort()
        possible_comb_num = []
        for num in nums:
            if num>ans: break
            possible_comb_num.append(num)
        
        self.ans = 0
        n = len(possible_comb_num)

        def backtrack(i, bor):
            if bor==ans:
                self.ans += 1
            if i==n:
                return
            
            for j in range(i, n):
                backtrack(j+1, bor|possible_comb_num[j])

        backtrack(0, 0)
        return self.ans

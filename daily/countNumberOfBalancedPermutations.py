class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD =  1_000_000_007
        n = len(num)
        num = list(map(int, num))
        tot = sum(num)
        if tot%2: return 0 # sum is odd can't create permutation
        target = tot//2
        cnt = Counter(num)
        max_odd = (n+1)//2
        psum = [0]*11
        for i in range(9, -1, -1):
            psum[i] = psum[i+1]+cnt[i] # create count of all digit from i to 9 at psum[i]
        
        @cache
        def dfs(digit, curr_sum, odd_cnt):
            if odd_cnt < 0 or psum[digit] < odd_cnt or curr_sum > target:
                return 0
            if digit > 9: return int(curr_sum == target and odd_cnt == 0)

            even_cnt = psum[digit] - odd_cnt
            res = 0
            for i in range(max(0, cnt[digit]-even_cnt), min(cnt[digit], odd_cnt)+1):
                ways = comb(odd_cnt, i) * comb(even_cnt, cnt[digit]-i) % MOD
                res += ways * dfs(digit+1, curr_sum + i*digit, odd_cnt-i)
            
            return res % MOD
            
        return dfs(0, 0, max_odd)

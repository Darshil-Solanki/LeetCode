class Solution:
    def longestBalanced(self, s: str) -> int:
        prefix_zero, prefix_one = [], []
        prefix_map = defaultdict(list)
        ind0_map, ind1_map = {}, {}
        ans = 0
        total_zero, total_one = 0, 0
        prefix_map[0].append(-1)

        for i, c in enumerate(s):
            if c == "1":
                total_one += 1
            else:
                total_zero += 1
            prefix_zero.append(total_zero)
            prefix_one.append(total_one)


        diff = 0
        for i, c in enumerate(s):
            if c == "1":
                diff += 1
            else:
                diff -= 1
            if diff in prefix_map:
                j = prefix_map[diff][0]
                ans = max(ans, i-j)
            if diff+2 in prefix_map:
                j = prefix_map[diff+2][0]
                one_inside = prefix_one[i] - (prefix_one[j] if j>-1 else 0)
                if total_one>one_inside:
                    ans = max(ans, i-j)
                elif diff+2 in ind1_map:
                    ans = max(ans, i-ind1_map[diff+2])
            if diff-2 in prefix_map:
                j = prefix_map[diff-2][0]
                zero_inside = prefix_zero[i] - (prefix_zero[j] if j>-1 else 0)
                if total_zero>zero_inside:
                    ans = max(ans, i-j)
                elif diff-2 in ind0_map:
                    ans = max(ans, i-ind0_map[diff-2])
            prefix_map[diff].append(i)
            if diff not in ind0_map and prefix_zero[i]>0:
                ind0_map[diff] = i
            if diff not in ind1_map and prefix_one[i]>0:
                ind1_map[diff] = i
        
        return ans

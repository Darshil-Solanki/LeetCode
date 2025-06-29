class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        if n==1: return [0]
        elif n==2: return [0, 0]
            
        ans = [0]*n
        left_max = [0]*n
        right_max = [0]*n
        cache = [0]*(n-1)

        @lru_cache
        def get_length_common_prefix(a, b):
            cl = 0
            for ac, bc in zip(a,b):
                if ac!=bc:
                    break
                cl += 1
            return cl
            
        for i in range(n-1):
            a, b = words[i], words[i+1]
            l = get_length_common_prefix(a, b)
            cache[i] = l
            if not i:
                left_max[i] = l
            else:
                left_max[i] = max(left_max[i-1], l)

        for i in range(n-2, -1, -1):
            right_max[i] = max(cache[i], right_max[i+1])

        ans[0] = right_max[1]
        ans[n-1] = left_max[n-3]

        for i in range(1, n-1):
            removed_i = get_length_common_prefix(words[i-1], words[i+1])
            left = 0 if i == 1 else left_max[i-2]
            right = right_max[i+1]
            ans[i] = max(left, right, removed_i)

        return ans
